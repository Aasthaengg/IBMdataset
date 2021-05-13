n=int(input())
a=list(map(int,input().split()))
x1=sum(a)
for i in range(n):
  if i%2!=0:
    x1-=2*a[i]
ans=[x1]
for i in range(n-1):
  ans.append(2*a[i]-ans[i])
print(*ans)