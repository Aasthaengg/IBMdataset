a,b,c =map(str, input().split())
A = int(a)
C = int(c)
res = 0
if b == "+":
  res = A+C
else:
  res = A-C
print(res)