a, b, c = input().split()
if a[-1] != b[0]:
  print("NO")
elif b[-1] != c[0]:
  print("NO")
else:
  print("YES")