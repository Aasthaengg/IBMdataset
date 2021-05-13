import sys
import math

def is_capable(n, k, w, P):
    track = 0
    cnt = 0
    i = 0

    while cnt < k:
        if i == n:
            return i

        if track + w[i] > P:
            track = 0
            cnt += 1
        else:
            track += w[i]
            i += 1

    return i
    pass

# ??\?????¨
n, k = map(int, sys.stdin.readline().split())
w = []
for i in range(n):
    w.append(int(sys.stdin.readline().strip()))

'''
print(n,k)
print(w)
'''

# ????????¨

if k == 1:
    ans = sum(w)
    print(ans)
elif n == 1:
    ans = w[0]
    print(ans)
else:
    max_p = sum(w)
    min_p = math.ceil(max_p / k) - 1

    # print(max_p, min_p)
    # sys.exit(0)
    
    bottom = min_p
    top = max_p

    while top - bottom > 1:
        mid = (bottom + top) // 2

        if is_capable(n, k, w, mid) == n:
            top = mid
        else:
            bottom = mid

    print(top)