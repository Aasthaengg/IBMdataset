N, X = map(int, input().split())
M =[int(input()) for i in range(N)]
X -= sum(M)
M.sort()
n = N
while X >= M[0]:
  n += 1
  X -= M[0]
print(n)
