n = int(input())
s = 0
m = 0
for _ in range(n):
  a = int(input())
  m = max(a,m)
  s += a
print(s - m//2)