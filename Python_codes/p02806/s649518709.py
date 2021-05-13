n = int(input())
d = {}
sum_ = 0
for i in range(n):
  s, t = map(str, input().split())
  t = int(t)
  sum_ += t
  d[s] = sum_
x = str(input())
print(d[s]-d[x])