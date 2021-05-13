N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [0 for i in range(N + 1)]

for a in A:
    B[a] += 1
nums = [b for b in B if b > 0]
nums.sort()
n = len(nums)
print(0 if n<=K else sum(nums[:n - K]))
