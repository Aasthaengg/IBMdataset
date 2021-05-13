nums = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 使うマッチ棒の本数が等しい場合は大きい数だけ考えれば良い
A.sort(reverse=True)
s = set()
candidates = [] # [a, nums[a]]
for a in A:
  if nums[a] in s:
    continue
  s.add(nums[a])
  candidates.append([a, nums[a]])


dp = [-1] * (N+1)
dp[0] = 0
for i in range(N+1):
  for a, n in candidates:
    if i >= n and dp[i-n]>=0:
      dp[i] = max(dp[i], dp[i-n]+1)

ans = ''
idx = N
digit = dp[N]
while digit:
  for a, n in candidates:
    if idx - n >= 0 and dp[idx-n] == dp[idx]-1:
      ans += str(a)
      digit -= 1
      idx -= n
      break

print(int(ans))