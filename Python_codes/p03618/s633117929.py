from collections import Counter
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def solve():
    S = input()[:-1]
    N = len(S)
    C = Counter(S)
    ans = 0
    for v in C.values():
        ans += v*(v-1)//2
    print(N*(N-1)//2-ans+1)


solve()
