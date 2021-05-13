N = int(input())
L = []

for _ in range(N):
  d = int(input())
  L.append(d)

print(len(set(L)))