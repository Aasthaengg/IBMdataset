n = int(input())
a = []

for _ in range(n):
  aa, b = map(int,input().split())
  if aa == b:
    a.append("1")
  else:
    a.append("0")
if "111" in "".join(a):
  print("Yes")
else:
  print("No")