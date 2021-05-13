from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))

total = sum(a)
cum_sum = list(accumulate(a))

ans = float("INF")
for former in cum_sum:
    ans = min(ans, abs(former - (total - former)))
print(ans)