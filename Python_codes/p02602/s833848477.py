import sys
input = sys.stdin.readline
INF = 10**18
def li():
    return [int(x) for x in input().split()]

N, K = li()
A = [0] + li()
for i in range(1, N-K+1):
    if A[K+i] > A[i]:
        print("Yes")
    else:
        print("No")