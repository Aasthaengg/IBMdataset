import sys
sys.setrecursionlimit(10**6)

K = int(input())
A = list(map(int,input().split()))

def ceil(a, b):
    return -(-a // b)

def floor(a, b):
    return a // b

def L(i):
    if i == K:
        return 2
    return ceil(L(i+1), A[i]) * A[i]

def R(i):
    if i == K:
        return 2
    return floor(R(i+1), A[i]) * A[i] + A[i] - 1

L0 = L(0); R0 = R(0)
if L0 <= R0:
    print(L0, R0)
else:
    print(-1)