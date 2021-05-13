N = int(input())
L = [0] * N
for i in range(N):
  s, p = map(str, input().split())
  p = -1 * int(p)
  L[i] = [s, p, i + 1]
L = sorted(L)
#print(L)
for i in range(N):
  print(L[i][2])
