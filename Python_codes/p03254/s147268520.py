n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
count = 0
for i in range(n-1):
  if a[i] <= x:
    x = x - a[i]
    count += 1
if a[n-1] == x:
  count += 1
    
print(count)