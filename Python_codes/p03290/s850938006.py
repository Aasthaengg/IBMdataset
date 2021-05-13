import sys
readline = sys.stdin.readline

D,G = map(int,readline().split())
P = [0] * D
C = [0] * D
for i in range(D):
  P[i],C[i] = map(int,readline().split())

# 全部解く問題をどれにするか、全探索

ans = 10 ** 9
for i in range(2 ** D):
#  print("bin(i)",bin(i)[2:].zfill(2))
  score = 0
  solve = 0
  for j in range(D):
    if (i >> j) & 1:
      score += P[j] * (j + 1) * 100 + C[j]
      solve += P[j]
#  print("score",score,"solve",solve)
  rest = G - score
#  print("score",score,"rest",rest)

  # 残りの点数を、高いほうから埋めていく
  if rest <= 0:
    if ans > solve:
      ans = solve
    continue
  for j in range(D - 1,-1,-1):
    if (i >> j) & 1 == 0:
      if (P[j] - 1) * (j + 1) * 100 == rest:
        solve += (P[j] - 1)
        rest = 0
        break
      if (P[j] - 1) * (j + 1) * 100 < rest:
        rest -= (P[j] - 1) * (j + 1) * 100
        solve += (P[j] - 1)
      else:
        p = (j + 1) * 100
#        print("p",p,"(rest + p - 1) // p",(rest + p - 1) // p)
        solve += (rest + p - 1) // p
        rest = 0
        break
  if rest > 0:
    continue
  if solve < ans:
    ans = solve
#  print("ans",ans)
    
print(ans)
    

      
      
