from sys import stdin

def Check(P):
    j = 0
    for _ in range(k):
        s = 0
        while s + W[j] <= P:
            s += W[j]
            j += 1
            if j == n:
                return j
    return j

def Solve():
    l = 0
    r = 100000 * 100000
    while r - l > 1:
        m = (l + r) // 2
        v = Check(m)
        if v == n:
            r = m
        else:
            l = m
    return r

n, k = map(int, stdin.readline().split())
W = [int(x) for x in stdin.readlines()]

print(Solve())
