import sys
from operator import itemgetter

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def iif(n): return [int(input()) for _ in range(n)]
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():
    mod = 1000000007

    F = [1, 1]
    for i in range(100000):
        F.append(F[i] + F[i+1])

    N, M = mi()

    if M == 0:
        print(F[N] % mod)
        return

    A = iif(M)
    DA = []
    left = 0
    for i in range(M):
        da = A[i] - left
        if da == 0 and left != 0:
            print(0)
            return
        else:
            DA.append(da-1)
        left = A[i] + 1
    if A[-1] != N:
        DA.append(N - A[-1] - 1)


    ans = 1
    for i in DA:
        ans *= F[i]

    print(ans % mod)

    return

main()
