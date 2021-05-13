h, n = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in range(n):
  c = c + a[i]
if (c >= h):
  print("Yes")
else:
  print("No")