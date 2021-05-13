import os
import os
import sys
from collections import defaultdict

from scipy.misc import comb

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

S = sys.stdin.readline().rstrip()
N = len(S)


def test(S):
    s = {S}
    for l in range(len(S)):
        for r in range(l + 1, len(S)):
            s.add(S[:l] + S[l:r + 1][::-1] + S[r + 1:])
    return len(s)


ans = comb(len(S), 2, exact=True) + 1
counts = defaultdict(int)
for i, c in enumerate(S):
    # i より左にあるやつと c を選ぶと、その間の文字列を反転したのと同じになる
    ans -= counts[c]
    counts[c] += 1
print(ans)

# print(test(S))
