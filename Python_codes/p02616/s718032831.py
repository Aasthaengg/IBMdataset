n, k = map(int, input().split())
mod = 10 ** 9 + 7
from collections import deque

a = list(map(int, input().split()))
a.sort()
minus, zero, plus = 0, 0, 0
for i in range(n):
    if a[i] < 0:
        minus += 1
    elif a[i] == 0:
        zero += 1
    else:
        plus += 1

que = deque(a)

#ここを軽量化した
plus_flg = False
tmp = plus - k
if tmp >= 0:
    plus_flg = True
elif (-tmp <= minus and -tmp%2 == 0) or (-tmp < minus and plus >= 1):
    plus_flg = True

# plus可能
if plus_flg:
    ans = 1
    cnt = 0

    while cnt < k:
        if k - cnt >= 2:
            if que[0] * que[1] >= que[-1] * que[-2]:
                ans *= que.popleft()
                ans *= que.popleft()
                ans %= mod
                cnt += 2
            else:
                ans *= que.pop()
                ans %= mod
                cnt += 1
        else:
            ans *= que.pop()
            ans %= mod
            cnt += 1

    print(ans)



# zero
elif zero > 0:
    print(0)

# minus
else:
    a = [abs(a[i]) for i in range(n)]
    a.sort()
    ans = 1
    for i in range(k):
        ans *= a[i]
        ans %= mod
    ans = -ans % mod
    print(ans)
