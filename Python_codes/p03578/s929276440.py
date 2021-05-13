from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

memo = defaultdict(int)

for d in D:
    memo[d] += 1

for t in T:
    memo[t] -= 1

memo = list(memo.values())
memo.sort()

print("YES" if memo[0] >= 0 else "NO")