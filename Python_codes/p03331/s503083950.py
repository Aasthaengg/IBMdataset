n = int(input())
mn = float("inf")
for i in range(1,n):
  count = 0
  for s in str(i):
    count += int(s)
  for p in str(n-i):
    count += int(p)
  if count < mn:
    mn = count
print(mn)