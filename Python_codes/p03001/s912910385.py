import sys
from operator import itemgetter

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():
    W, H, x, y = mi()

    s = W*H/2
    cut = 1 if W/2 == x/1 and H/2 == y/1 else 0

    print(s, cut)

    return

main()
