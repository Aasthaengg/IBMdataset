N, M = map(int, input().split())
L = []
ans = 0
for i in range(N):
  L.append(list(map(int,input().split())))
L.sort()
for i in range(N):
  if L[i][1]<=M:
    M -= L[i][1]
    ans += L[i][0]*L[i][1]
  else:
    ans += L[i][0]*M
    break
print(ans)