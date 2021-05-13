n = int(input())
memo = [1, 1] + [0 for _ in range(n-1)]
for i in range(n+1):
    if not memo[i]:
        memo[i] = memo[i - 1] + memo[i - 2]
print(memo[-1])