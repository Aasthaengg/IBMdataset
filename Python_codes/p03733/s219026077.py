import sys
input = lambda: sys.stdin.readline().rstrip()
n, t = map(int, input().split())
query = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    interval = query[i] - query[i - 1]
    ans += min(t, interval)

# 最後の一回分
ans += t
print(ans)
