import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from itertools import combinations_with_replacement
def resolve():
    n, m, q = map(int, input().split())
    ABCD = [tuple(map(int, input().split())) for _ in range(q)]
    ans = 0
    for I in combinations_with_replacement(range(m), n):
        score = 0
        for a, b, c, d in ABCD:
            if I[b - 1] - I[a - 1] == c:
                score += d
        ans = max(ans, score)
    print(ans)
resolve()