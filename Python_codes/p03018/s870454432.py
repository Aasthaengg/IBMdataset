def sol(S):
  N = len(S)
  nums = [0 for _ in range(N+1)]
  i = N-1
  while i >= 0:
    if S[i-1:i+1] == 'BC':
      nums[i-1] = nums[i+1] + 1
      nums[i] = nums[i+1] + 1
      i -= 2
    else:
      nums[i] = nums[i+1]
      i -= 1
  ans = 0
  for i, s in enumerate(S):
    if s == 'A':
      ans += nums[i]
  return ans

S = input()
ans = 0
N = len(S)
si, i = 0, 0
while i < N:
  if S[i] == 'A':
    i += 1
  elif S[i:i+2] == 'BC':
    i += 2
  else:
    ans += sol(S[si:i+1])
    si = i + 1
    i += 1
ans += sol(S[si:])
print(ans)