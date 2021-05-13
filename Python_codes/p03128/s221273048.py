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


dp1 = [0] * (N+1)
dp2 = [-1] * (N+1)
d = {}
for a, n in candidates:
  if n <= N:
    dp1[n] = 1
    dp2[n] = 0
    d[n] = a

for i in range(N+1):
  for a, n in candidates:
    if i >= n and dp1[i-n]:
      if dp1[i] < dp1[i-n] + 1:
        dp1[i] = dp1[i-n] + 1
        dp2[i] = i-n

ans = []
idx = N
while idx:
  next_idx = dp2[idx]
  ans.append(d[idx - next_idx])
  idx = next_idx

ans.sort(reverse=True)
print(''.join(list(map(str, ans))))