import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

import bisect
a.sort()
c.sort()
ans = 0

for i in b:
    ans += bisect.bisect_left(a, i) * (len(c) - bisect.bisect_right(c, i))

print(ans)