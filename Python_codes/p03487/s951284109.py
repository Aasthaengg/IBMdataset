# https://atcoder.jp/contests/abc082/tasks/arc087_a
from collections import Counter
n = int(input())
nums = [int(i) for i in input().split()]
c = Counter(nums)


ans = 0
for k, v in c.items():
    if k > v:
        ans += v
    else:
        ans += (v - k)
print(ans)