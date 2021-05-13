n = int(input())
a = [int(x) for x in input().split()]
a.sort()
ans = [0]*(n-1)

k1, k2 = a[0], a[-1]
for i in range(1, n-1):
  if a[i] >= 0:
    ans[i-1] = (k1, a[i])
    k1 -= a[i]
  else:
    ans[i-1] = (k2, a[i])
    k2 -= a[i]
ans[n-2] = (k2, k1)
print(k2-k1)
for value in ans:
  print(*value)