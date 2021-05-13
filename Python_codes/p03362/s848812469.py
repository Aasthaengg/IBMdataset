import sys
readline = sys.stdin.readline

N = int(readline())

fact = [True] * 55556
fact[0] = False
fact[1] = False
ans = []
for i in range(len(fact)):
  if fact[i]:
    for j in range(i * 2, len(fact), i):
      fact[j] = False
    if i % 5 == 1:
      ans.append(i)
      if len(ans) == N:
        break
      
print(*ans)
      
