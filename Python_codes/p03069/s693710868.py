N = int(input())
S = input()

B_sum = [0]*(N+1)
for i in range(N):
  if S[i] == "#":
    B_sum[i+1] = B_sum[i] + 1
  else:
    B_sum[i+1] = B_sum[i]

ans = float("INF")
for i in range(N+1):
  b_cnt = B_sum[i]
  w_cnt = N - i - (B_sum[N] - B_sum[i])
  tmp = b_cnt + w_cnt
  ans = min(ans, tmp)
  
print(ans)