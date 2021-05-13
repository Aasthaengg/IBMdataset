N = int(input())
ABs = []
for i in range(N):
  X, L = map(int, input().split())
  A, B = X-L, X+L
  ABs.append((A, B))
ABs.sort(key=lambda AB: AB[1])
#print(ABs)
r = 1
b = ABs[0][1]
for i in range(1, N):
  A, B = ABs[i]
  if A >= b:
    r += 1
    b = B
print(r)
