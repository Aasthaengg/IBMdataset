n = int(input())
dat_a = list(map(int, input().split()))
dat_b = list(map(int, input().split()))
dat_c = list(map(int, input().split()))
dat_a.sort()
dat_b.sort()
dat_c.sort()

import bisect
res = 0
for i in range(n):
    x = bisect.bisect_left(dat_a, dat_b[i])
    y = bisect.bisect_right(dat_c, dat_b[i])
    res += x * (n - y)
print(res)