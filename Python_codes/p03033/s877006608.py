import sys
import bisect
input = sys.stdin.readline

n, q = map(int, input().split())
cons = [list(map(int, input().split())) for _ in range(n)]
d = [int(input()) for _ in range(q)]

cons.sort(key=lambda x: x[2])
for i in range(n):
    cons[i][0] -= cons[i][2]
    cons[i][1] -= cons[i][2]

ans = [-1] * q
l = [-1] * q
for i in range(n):
    s = bisect.bisect_left(d, cons[i][0])
    t = bisect.bisect_left(d, cons[i][1])
    while s < t:
        if l[s] != -1:
            s = l[s]
        else:
            ans[s] = cons[i][2]
            l[s] = t
            s += 1
print(*ans, sep="\n")