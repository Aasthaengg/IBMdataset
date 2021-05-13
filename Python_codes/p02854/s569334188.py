from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
cumsum = list(accumulate(a))
total = cumsum[-1]

ans = 10**20
for left in cumsum:
    right = total - left
    ans = min(ans, abs(left - right))

print(ans)