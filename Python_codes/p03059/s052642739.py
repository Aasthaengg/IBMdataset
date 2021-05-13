A, B, T = list(map(int, input().split()))
ans = 0
cnt = 1

while cnt < T+0.5:
  if cnt%A == 0:
    ans = ans + B
  cnt += 1
print(ans)