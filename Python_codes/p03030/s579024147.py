N = int(input())
L = []
for i in range(N):
  s, p = map(str, input().split())
  L.append([s, -int(p), i+1])
L = sorted(L)

for i in range(N):
  print(L[i][2])
