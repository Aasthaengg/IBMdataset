n, m, k = map(int, input().split())
if abs(n -m) < abs(n -k):
  print("A")
else:
  print("B")