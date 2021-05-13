n,k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])

nums = [0]*(n-k+1)
for i in range(n-k+1):
  nums[i] = h[i+k-1] - h[i]
print(min(nums))