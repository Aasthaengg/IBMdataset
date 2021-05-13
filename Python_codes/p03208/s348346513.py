N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()

nums = [None] * (N-K+1)
for i in range(N-K+1):
    nums[i] = H[i+K-1] - H[i]

print(min(nums))