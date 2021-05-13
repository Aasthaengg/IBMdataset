n,m = map(int, input().split())
count = 0
for i in range(n):
  k,l = map(int, input().split())
  t = ((k ** 2) + (l ** 2)) ** 0.5
  if t <= m:
    count += 1
print(count)