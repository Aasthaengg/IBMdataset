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
    
    N, Q = mi()
    S = input()
    AC_cnt = [0] * len(S)
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == "A" and S[i+1] == "C":
            cnt += 1
        AC_cnt[i+1] = cnt

    for i in range(Q):
        l, r = mi()
        print(AC_cnt[r-1] - AC_cnt[l-1])

    return

main()
