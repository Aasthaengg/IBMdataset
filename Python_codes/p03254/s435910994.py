n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
happy = 0
for i in range(n-1):
  if a[i] <= x:
    x -= a[i]
    happy += 1
  else:
    break
happy += 1 if x == a[n - 1] else 0
print(happy)
