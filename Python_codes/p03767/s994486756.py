n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
res = 0
for i in range(1, n * 2, 2):
  res += a[i]
print(res)
