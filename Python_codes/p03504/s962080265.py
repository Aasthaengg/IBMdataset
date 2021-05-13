from bisect import bisect_left
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
stc = [[int(i) for i in input().split()] for _ in range(N)]
stc.sort()
stc.sort(key=lambda x: x[2])
a = []
S, T, C = stc[0]
for s, t, c in stc[1:]:
    if c == C and T == s:
        T = t
    else:
        a.append((S, T, C))
        S, T, C = s, t, c
a.append((S, T, C))

a.sort(key=lambda x: x[1])
l = [a[0][1]]
for s, t, c in a[1:]:
    i = bisect_left(l, s)
    if 0 < i and l[i - 1] < s:
        l.pop(i - 1)
    l.append(t)
print(len(l))