s = int(input())
a = int(s/100)
c = s%10
d = (s-c)/10
b = d%10
if a ==7 or b ==7 or c ==7:
  print("Yes")
else:
  print("No")