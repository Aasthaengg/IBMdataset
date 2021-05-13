a, b, c =list(map(int, input().split()))

if (a+b+c)/2 == a or (a+b+c)/2 == b or (a+b+c)/2 == c:
  print("Yes")
elif (a+b+c)/2 == a+b or (a+b+c)/2 == b+c or (a+b+c)/2 == c+a:
  print("Yes")
else:
  print("No")