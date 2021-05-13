N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()
ans = 0
cnt = 0
for a, b in AB:
  if cnt == M:
    break
  
  if cnt + b <= M:
    ans += a * b
    cnt += b
  else:
    ans += a * (M - cnt)
    cnt += M - cnt

print(ans)