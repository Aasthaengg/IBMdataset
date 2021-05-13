n,k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
# 各数列A内での転倒数
for i in range(n):
  for j in range(i+1,n):
    if a[i] > a[j]: ans += 1
ans *= k

# k回の繰り返しによって発生する転倒数
a.sort()
nums = [0]*n
for i in range(1,n):
  if a[i] > a[i-1]: nums[i] = i
  else: nums[i] = nums[i-1]

ans += sum(nums)*k*(k-1)//2
ans %= 10**9+7
print(ans)