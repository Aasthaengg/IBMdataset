N, M = map(int, input().split())
inf =  10**9
brid = [inf]*N
for i in range(M):
  a, b =  map(int, input().split())
  brid[a-1] =min(b, brid[a-1])
right_side =  N+1
ans = 0
for i in range(N-1, -1, -1):
  if brid[i] == inf:
    continue
  else:
    if brid[i] <= right_side:
      ans += 1
      right_side = i+1
print(ans)    