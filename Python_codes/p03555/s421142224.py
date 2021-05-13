a=str(input())
b=str(input())
a=list(a)
b=list(b)
if a == b[::-1]:
  print("YES")
else:
  print("NO")