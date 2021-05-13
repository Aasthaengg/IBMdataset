S,C=map(int,input().split())
ANS = 0
if S * 2 <= C:
  ANS = S
  C -= (S*2)
  #rint(C)
  ANS += (C//4)
  print(ANS)
else:
  ANS = C // 2
  print(ANS)