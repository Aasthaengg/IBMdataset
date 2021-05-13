A,B,N=map(int,input().split())

ans=-100000
for x in range(A):
  #print(A//B,x//B,A*x//B,A*x//B-A*(x//B))
  ans=max(ans,(A*x//B)-A*(x//B))
  if x==N:break
x=B-1
if x>N:x=N
ans=max(ans,(A*x//B)-A*(x//B))
print(ans)