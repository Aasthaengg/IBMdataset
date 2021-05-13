a,b,c = [int(a) for a in input().split()]
if a==b and b==c and a==c:
  print("No")
elif a==b or b==c or a==c:
  print("Yes")
else:
  print("No")  