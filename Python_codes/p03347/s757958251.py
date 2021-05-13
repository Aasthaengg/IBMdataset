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
A = [int(sys.stdin.buffer.readline()) for _ in range(N)]

# 最初が0じゃないとだめ
if A[0] > 0:
    print(-1)
    exit()
ans = 0
for a, b in zip(A, A[1:]):
    if a + 1 < b:
        print(-1)
        exit()
    if a + 1 == b:
        ans += 1
    elif b > 0:
        ans += b
print(ans)
