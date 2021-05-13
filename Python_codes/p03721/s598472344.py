# https://atcoder.jp/contests/abc061/tasks/abc061_c
from collections import defaultdict

n, k = [int(i) for i in input().split()]
d = defaultdict(int)

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    d[a] += b

array = sorted(d.items(), key=lambda x: x[0])
for num, count in array:
    if k > count:
        k -= count
    else:
        print(num)
        quit()
