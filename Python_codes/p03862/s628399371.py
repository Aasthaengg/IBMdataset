n, x = map(int, input().split())
a = [int(x) for x in input().split()]
ans = 0
for i in range(n-1):
  if a[i]+a[i+1] > x:
    k = min([a[i+1], a[i]+a[i+1]-x])
    a[i+1] -= k
    ans += k
    if a[i] > x:
      ans += a[i]-x
      a[i] = x

print(ans)