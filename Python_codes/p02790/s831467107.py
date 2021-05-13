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
    a, b = ss()
    sa = a*int(b)
    sb = b*int(a)

    if sa <= sb:
        print(sa)
    else:
        print(sb)

    return

main()
