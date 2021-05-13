n =int(input())
a = list(map(int,input().split()))
c = [0 for _ in range(n+1)]
ans = 0
for i in range(n):
  if a[i] <= n:
    c[a[i]] += 1
  else:
    ans += 1
for i in range(n+1):
  if c[i] >= i:
    ans += c[i] - i
  else:
    ans += c[i]
print(ans)

