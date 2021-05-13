N, C, K = map(int, input().split())
T = []
for i in range(N):
  t = int(input())
  T.append(t)
  
T.sort()
ans = 1
cnt = 0
time = T[0]
for t in T:
  if (t<=time+K) and (cnt<C):
    cnt += 1
  else:
    ans += 1
    cnt = 1
    time = t
print(ans)