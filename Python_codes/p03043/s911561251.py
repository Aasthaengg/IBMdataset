import sys
from operator import itemgetter
import math

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():
    n, k = mi()

    ans = 0
    for i in range(1, n+1):
        t = 0
        while i < k:
            i *= 2
            t += 1
        ans += 0.5 ** t
    ans /= n
    print(f"{ans:.12f}")
    return

main()
