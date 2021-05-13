import bisect
import sys

N,C,K=map(int,input().split())
T=[int(input()) for _ in range(N)]
T.sort()
ans=0
i=0

if T[0]+K>=T[-1]:
  if N%C==0:
    print(N//C)
  else:
    print(N//C+1)
  sys.exit()
else:
  while True:
    t=bisect.bisect_right(T,T[i]+K)
    if t-i>C:
      i+=C
    else:
      i=t
    ans+=1
    if i==N-1:
      ans+=1
      break
    if i>N-1:
      i=N-1
      break
print(ans)