import sys
import fractions
import bisect
input=sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

ans = 0
k = 0
for j in b:
    ai = bisect.bisect_left(a, j)
    ci = n - bisect.bisect_right(c, j)
    ans += ai * ci
print(ans)
