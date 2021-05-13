import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

s = ns()
s = list(s)
asc = range(97,123)

import bisect

if len(s) < 26:
    ss = [ord(u) for u in s]
    for i in asc:
        if i not in ss:
            s.append(chr(i))
            print(''.join(s))
            exit()
else:
    ss = s[::-1]
    a = [ord(ss[0])]
    for i in range(1,len(ss)):
        j = ord(ss[i])
        if j > a[-1]:
            a.append(j)
        else:
            k = bisect.bisect_right(a,j)
            x = chr(a[k])
            sss = s[:26-(i+1)] + [x]
            print(''.join(sss))
            exit()
    print(-1)
