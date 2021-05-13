l = list(input())
l.sort()
a,b,c,d = l
if a == b and b != c and c == d:
  print("Yes")
else:
  print("No")