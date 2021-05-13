n, t = map(int, input().split())
a = [int(x) for x in input().split()]

minimum = a[0]
count = 0
profit = 0
for i in range(1, n):
  if a[i] < minimum:
    minimum = a[i]
    continue
  
  k = a[i]-minimum
  if profit < k:
    profit = k
    count = 1
  elif profit == k:
    count += 1

print(count)