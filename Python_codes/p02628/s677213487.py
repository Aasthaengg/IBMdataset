N, M = map(int, input().split())
p = list(map(int, input().split()))
a = sorted(p, reverse=False)
c = 0
for b in a[:M]:
  c = c + b
print(c)