A,B,T=map(int,input().split())
ans=0
for x in range(T//A):
  ans+=B
print(ans)