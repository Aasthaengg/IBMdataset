a,b = map(int, input().split(" "))
b = b -1
if b==0:
  print("YES")
elif (a-1)//b >=2:
  print("YES")
else:
  print("NO")
