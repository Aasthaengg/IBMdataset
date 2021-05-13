from collections import Counter
N=int(input())
A=list(input())
B=list(input())
C=list(input())

ans=0
for i in range(N):
  c=list(Counter([A[i],B[i],C[i]]).values())
  if c==[1,1,1]:
    ans+=2
  elif c==[2,1] or c==[1,2]:
    ans+=1
  else:
    pass
print(ans)