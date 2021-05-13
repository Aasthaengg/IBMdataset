A = int(input())
p = A % 10
A //= 10
q = A % 10
A //= 10
r = A % 10
s = A // 10
if p == q == r or q == r == s:
  print("Yes")
else:
  print("No")