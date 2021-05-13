import bisect

N,K = map(int,input().split())
A = list(map(int,input().split()))

# dp[i]:残りの石がi個の時、先手が負けなら0、勝ちなら1
dp = [0 for _ in range(K+1)]

for i in range(1,K+1):
  rank = bisect.bisect_right(A, i)
  if rank == 0:
    dp[i] = 0
  else:
    for j in range(rank):
      if i-A[j] >= 0 and dp[i-A[j]] == 0:
        dp[i] = 1
        break
print('First' if dp[K] == 1 else 'Second')
