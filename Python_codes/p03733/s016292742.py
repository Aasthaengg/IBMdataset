n,t = map(int,input().split())
a = list(map(int,input().split()))
ans = t
l = a[0]
for i in range(1,n):
  ans += min(t,a[i]-l)
  l = a[i]
print(ans)