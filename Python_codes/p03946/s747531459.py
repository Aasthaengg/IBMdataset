n,T = map(int,input().split())

a = list(map(int,input().split()))
maxDiff = 0
curMin = a[0]
for i in range(n):
  if curMin > a[i]:
    curMin = a[i]
  if maxDiff < a[i] - curMin:
    maxDiff = a[i] - curMin

isCovered = False
count = 0

curMin = a[0]

for i in range(n):
  if curMin > a[i]:
    curMin = a[i]
    isCovered = False
  if maxDiff == a[i] - curMin:
    if not isCovered:
      count += 1
      isCovered = True

print(count)
