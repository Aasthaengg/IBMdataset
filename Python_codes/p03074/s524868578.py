N, K = [int(c) for c in input().split()]
S = input()

nums = []
cnt = 1
if S[0] == "0":
  nums.append(0)
for i in range(N):
  if i == N-1 or S[i] != S[i+1]:
    nums.append(cnt)
    cnt = 1
  else:
    cnt += 1
if S[-1] == "0":
  nums.append(0)

Sum = [0]*(len(nums)+1)
for i in range(1, len(nums)+1):
  Sum[i] = Sum[i-1] + nums[i-1]

ans = 0
if len(nums) <= 2*K+1:
  ans = N
else:
  for i in range(0, len(nums) - 2*K+1, 2):
    ans = max(ans, Sum[i+2*K+1] - Sum[i])

print(ans)