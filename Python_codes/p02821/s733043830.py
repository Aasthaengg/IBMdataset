from itertools import accumulate
import sys
import bisect

input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse = True)

li = [0] * (2*10**5+1)

for i in a:
    li[i] += 1

acm = list(accumulate(li))
acm_a = list(accumulate(a))

l = 0
r = 2 * 10 ** 5

while l <= r:
    mid = (l + r) // 2
    count = 0
    for i in a:
        if mid - i >= 0:
            count += n - acm[mid-i]
        else:
            count += n
    if count >= m:
        l = mid + 1
    else:
        r = mid - 1

sum_idx = 0
ans = 0
b = a[::-1]
for left in a:
    right_min = l - left
    idx = bisect.bisect_left(b,right_min)
    if n - idx > 0:
        sum_idx += n - idx
        ans += left * (n - idx) + acm_a[n - idx - 1]

ans -= l * (sum_idx - m)

print(ans)
