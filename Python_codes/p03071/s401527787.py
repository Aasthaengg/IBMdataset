a, b = map(int, input().split())
s = max(a, b)
if a < b:
  b -= 1
else:
  a -= 1
t = max(a, b)
print(s + t)