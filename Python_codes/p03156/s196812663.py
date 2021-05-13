n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
ans = 0
c = 0
d = 0
e = 0
for i in range(n):
  if p[i] <= a:
    c += 1
  elif a + 1 <= p[i] <= b:
    d += 1
  elif p[i] >= b + 1:
    e += 1
ans = min(c, d, e)
print(ans)