l = list(map(int, input().split()))
if set([1, 9, 7, 4]).issubset(l):
  print("YES")
else:
  print("NO")