N, C, K = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()
ans = 1
p_cnt = 0
last_b = P[0]
for p in P:
  if p <= last_b+K and p_cnt < C:
    p_cnt += 1
  else:
    last_b = p
    p_cnt = 1
    ans += 1
print(ans)
