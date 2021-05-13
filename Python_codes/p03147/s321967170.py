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
    
    N = ii()
    H = lmi()
    F = [0] * N # flowers

    cnt = 0
    l, r = 0, 0
    while True:
        while H[l] == F[l]:
            l += 1
            if l == N:
                break
        if l == N:
            break
        for i in range(l, N):
            if H[i] == F[i]:
                r = i
                break
            if i == N-1:
                r = N
        for i in range(l, r):
            F[i] += 1
        cnt += 1
    
    print(cnt)

    return

main()
