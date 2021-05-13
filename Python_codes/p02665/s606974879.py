import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    not_leaf = 1
    s = sum(A)
    count = 1
    for d in range(n + 1):
        res += not_leaf
        if not_leaf < A[d]:
            print(-1)
            return
        not_leaf -= A[d]
        add = min(s - count, not_leaf)
        count += add
        not_leaf += add

    print(res if not_leaf == 0 else -1)
resolve()