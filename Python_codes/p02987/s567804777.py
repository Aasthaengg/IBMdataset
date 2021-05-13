s = list(input())
a = s[0]
b = s[1]
c = s[2]
d = s[3]

if a == b and c ==d and a!=c:
  print("Yes")
elif a == c and b == d and a != b:
  print("Yes")
elif a == d and b == c and a != c:
  print("Yes")
else:
  print("No")
