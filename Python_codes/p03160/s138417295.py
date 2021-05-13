n = int(input())
H = list(map(int, input().split()))

memo = [0 for _ in range(n)]
memo[1] = abs(H[1] - H[0])
for i in range(2, n):
  memo[i] = min(memo[i-1] + abs(H[i] - H[i-1]), memo[i-2] + abs(H[i] - H[i-2]))
print(memo[-1])