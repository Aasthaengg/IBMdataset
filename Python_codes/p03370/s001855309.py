N, X = list(map(lambda a: int(a), input().split(" ")))
m = []
for i in range(N):
  m.append(int(input()))
m.sort()

print(len(m) + (X - sum(m)) // m[0])