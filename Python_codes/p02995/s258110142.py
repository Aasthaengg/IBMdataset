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
    A, B, C, D = mi()
    A -= 1
    CD_lcm = C * D // math.gcd(C, D)
    ans = B - B//C - B//D + B//CD_lcm
    ans -= A - A//C - A//D + A//CD_lcm
    print(ans)
    return

main()
