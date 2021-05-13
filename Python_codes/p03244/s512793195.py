import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    n = int(input())
    odd = Counter()
    even = Counter()
    for i, a in enumerate(map(int, input().split())):
        if i & 1:
            odd[a] += 1
        else:
            even[a] += 1
    odd[-1] = even[-1] = 0

    res = n
    for key0, val0 in odd.most_common()[:2]:
        for key1, val1 in even.most_common()[:2]:
            if key0 != key1:
                res = min(res, n - val0 - val1)
    print(res)
resolve()