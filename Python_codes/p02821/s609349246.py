import sys
from itertools import accumulate
n, m = [int(i) for i in sys.stdin.readline().split()]
a_ls = [int(i) for i in sys.stdin.readline().split()]
a_ls.sort(reverse=True)
ls = [0 for i in range(10**6)]
for a in a_ls:
    ls[a+1] += 1
ls = [i for i in accumulate(ls)]

def check(x):
    res = 0
    for a in a_ls:
        res += n - ls[max(0,x - a)]
    return res

up = 10**6
down = 0
while True:
    mid = (up + down) // 2
    if check(mid) >= m:
        if down == mid:
            break
        down = mid
    else:
        if up == mid:
            if check(up) == m:
                mid = up
            break
        up = mid

acc_ls = [i for i in accumulate([0] + a_ls)]
ans = 0
for a in a_ls:
    x = n - ls[max(0, mid - a)]
    ans += x * a + acc_ls[x]
print(ans - (check(mid) - m) * mid)