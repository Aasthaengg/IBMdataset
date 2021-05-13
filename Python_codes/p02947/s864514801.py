import sys
from operator import itemgetter
from collections import Counter
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():
    N = ii()
    S = Counter()
        
    for s in [input().rstrip() for _ in range(N)]:
        s = list(s)
        s.sort()
        s = "".join(s)
        S[s] += 1

    ans = 0
    for n in S.values():
        ans += (n * (n-1)) // 2

    print(ans)

    return

main()
