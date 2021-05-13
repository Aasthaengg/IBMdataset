# 1 <= N <= 10**5
# N <= M <= 10**9
import sys
input = sys.stdin.buffer.readline
N, M = map(int, input().split())

V = M // N

ans = 1
for i in range(1, V + 1):
    if i * i > M:
        break
    if M % i == 0:
        j = M // i
        if j <= V:
            ans = max(ans, j)
        else:
            ans = max(ans, i)
print(ans)
