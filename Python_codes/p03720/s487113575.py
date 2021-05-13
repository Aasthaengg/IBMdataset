n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split()) 
    ab += [a, b]

for i in range(n):
  print(ab.count(i + 1))