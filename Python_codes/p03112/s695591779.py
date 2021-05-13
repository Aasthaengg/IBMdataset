import numpy as np
import sys
input = sys.stdin.buffer.readline

a, b, q = map(int,input().split())
ab = [[-1, -10**11], [-1, 10**11]]
aa = [-10**11, 10**11]
bb = [-10**11, 10**11]
for i in range(a):
    x = int(input())
    ab.append([0, x])
    aa.append(x)
    
for i in range(b):
    x = int(input())
    ab.append([1, x])
    bb.append(x)
ab = sorted(ab, key=lambda x:(x[1], x[0]))
aa.sort()
bb.sort()

ab_arr = np.array(ab)
ab_arr = ab_arr.T[1]

a_arr = np.array(aa)
b_arr = np.array(bb)

for cq in range(q):
    ans = 10**12
    s = int(input())
    ci = np.searchsorted(ab_arr, s)
    for cj in [ci, ci-1]:
        d = abs(ab_arr[cj] - s)
        flg = ab[cj][0]
        if flg:
            na = np.searchsorted(a_arr, ab_arr[cj])
            d2 = min(abs(a_arr[na] - ab_arr[cj]), abs(a_arr[na-1] - ab_arr[cj]))
            d += d2
        else:
            nb = np.searchsorted(b_arr, ab_arr[cj])
            d2 = min(abs(b_arr[nb] - ab_arr[cj]), abs(b_arr[nb-1] - ab_arr[cj]))
            d += d2
        ans = min(ans, d)
    print(ans)