n = int(input())
s = 0
for i in range(n):
  a, b = map(str, input().split())
  c = float(a)
  if b != "JPY":
    c = c * 380000.0
  s = c + s
print(s)