N = int(input())
a = N // 1000
N %= 1000
b = N //100
N %= 100
c = N // 10
N %= 10
d = N
if a == b and b == c:
  print("Yes")
elif b == c and c == d:
  print("Yes")
else:
  print("No")