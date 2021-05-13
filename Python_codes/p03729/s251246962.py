a, b, c = input().split()

d = len(a)-1
e = len(b)-1

if a[d] == b[0] and b[e] == c[0]:
  print("YES")
else:
  print("NO")