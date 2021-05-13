N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=0
while 1:
  if N>K:
    N -= (K-1)
    ans+=1
  else:
    ans+=1
    break
print(ans)
