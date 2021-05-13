n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a)
ans=0
for i in range(1,k+1):
  ans+=b[(-1)*i]
print(ans)
