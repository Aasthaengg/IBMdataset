import sys

N=int(input())
S=[int(input()) for _ in range(N)]
S.sort()
ans=sum(S)

if ans%10!=0:
  print(ans)
  sys.exit()
else:
  for i in range(N):
    if S[i]%10!=0:
      print(ans-S[i])
      sys.exit()
  else:
    print(0)