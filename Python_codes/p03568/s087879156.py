import sys
sys.setrecursionlimit(10**8)

n = int(input())
A = list(map(int, input().split()))

def f(i, v):
    if i == n:
        return any(x % 2 == 0 for x in v)

    ans = 0
    for d in (-1, 0, 1):
        v_ = v[:]
        v_.append(A[i]+d)
        ans += f(i+1, v_)

    return ans

print(f(0, []))