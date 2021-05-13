n, x = map(int, input().split())
a = list(map(int, input().split()))
l = [0] * (n+1)
for i in range(n):
  l[i+1] = l[i] + a[i]
ans = 0
for i in l:
  if i <= x:
    ans += 1
print(ans)