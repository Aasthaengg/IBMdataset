N, X = map(int, input().split())
L = [int(l) for l in input().split()]
if sum(L) <= X:
  print(N+1)
  exit()
D = 0
ans = 1
for i in range(N):
  D += L[i]
  if D <= X:
    ans += 1
  else:
    print(ans)
    exit()
