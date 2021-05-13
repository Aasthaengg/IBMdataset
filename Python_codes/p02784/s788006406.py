h, n = map(int, input().split())
a = list(map(int, input().split()))

aa = sum(a)

if aa >= h:
  print("Yes")
else:
  print("No")