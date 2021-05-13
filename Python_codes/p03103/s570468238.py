from bisect import bisect_left
from itertools import accumulate

N, M = map(int, input().split())
shop = [list(map(int, input().split())) for _ in range(N)]
shop.sort(key=lambda x: x[0])

cnt = 0
ans = 0

for i in range(N):
    cnt += shop[i][1]
    if M <= cnt:
        dif = cnt - M
        ans += shop[i][0] * shop[i][1] - dif * shop[i][0]
        break
    else:
        ans += shop[i][0] * shop[i][1]

print(ans)