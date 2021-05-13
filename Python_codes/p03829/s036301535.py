N,A,B=map(int,input().split())
X=list(map(int,input().split()))
ans=0
for i in range(len(X)-1):
  c = A*(X[i+1]-X[i])
  if c < B:
    ans+=c
  else:
    ans+=B
print(ans)