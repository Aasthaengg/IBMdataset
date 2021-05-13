l = list(map(int, input().split()))
l.sort()
a,b,c = l
if a+b == c:
  print("Yes")
else:
  print("No")