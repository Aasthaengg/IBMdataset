N, C, K = list(map(int, input().split()))
T = [int(input()) for _ in range(N)]

T.sort()

ans = 1
cnt = 1
t = T[0]

for i in range(1, N):
  if T[i] - t > K or cnt >= C:
    ans += 1
    cnt = 1
    t = T[i]
  else:
    cnt += 1

print(ans)