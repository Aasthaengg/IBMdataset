N = int(input())
d = {}
for i in range(N):
  a = int(input())
  d[a] = d.get(a, 0) ^ 1
x = sorted(d.values())
print(sum(x))