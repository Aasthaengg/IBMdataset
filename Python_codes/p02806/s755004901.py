import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N = int(sys.stdin.buffer.readline())
S, T = list(zip(*[sys.stdin.buffer.readline().decode().rstrip().split() for _ in range(N)]))
X = sys.stdin.buffer.readline().decode().rstrip()
T = list(map(int, T))

i = S.index(X)
ans = sum(T[i + 1:], 0)
print(ans)
