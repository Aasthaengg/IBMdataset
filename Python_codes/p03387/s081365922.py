a = list(map(int,input().split()))
a.sort()
x = 2 * max(a) - a[0] - a[1]
if x%2 == 0:
  print(x // 2)

else:
  print(x // 2 + 2)
