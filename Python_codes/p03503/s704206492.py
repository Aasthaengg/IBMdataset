n=int(input())
f=['' for _ in range(n)]
p=[[] for _ in range(n)]
for i in range(n):
  f[i]=int(''.join(input().split()),2)
for i in range(n):
  p[i]=list(map(int,input().split()))
ans=-10**9
for i in range(1,1024):
  tmp=0
  for j in range(n):
    k=str(format(i&f[j],'010b')).count('1')
    tmp+=p[j][k]
  ans=max(ans,tmp)
print(ans)