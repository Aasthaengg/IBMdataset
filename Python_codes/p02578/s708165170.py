n = int(input())
a = list(map(int,input().split()))
s = a[0]
ans = 0
for i in range(1,n):
  ans += max(0,s-a[i])
  s = max(s,a[i])
print(ans)
