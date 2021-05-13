import sys
n, k = list(map(int, input().split()))

ws = list(map(int, sys.stdin.read().split()))

def check(A, n, k, mid):
    j = 0
    for i in range(k):
        p = mid
        s = 0
        while (s + A[j]) <= p:
            s += A[j]
            j += 1
            if ( j == n ):
                return n
    return j

def solve(A, n, k):
    h = 100000 * 10000
    l = 0
    while 1 < (h - l):
        mid = (h + l) // 2
        v = check(A, n, k, mid)
        if v < n:
            l = mid
        else:
            h = mid
    return h

print(solve(ws, n, k))