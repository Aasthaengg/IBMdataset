import sys
n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
count = 0
for i in range(n):
  if x >= a[i]:
    x -= a[i]
    count += 1
    if i == n-1 and x > 0:
      print(count-1)
      sys.exit()
    elif i == n-1 and x == 0:
      print(count)
      sys.exit()
  else:
    print(count)
    sys.exit()