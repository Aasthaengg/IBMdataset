import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


S = sys.stdin.buffer.readline().decode().rstrip()

a = 0
ab = 0
abc = 0
q = 0
for i, s in enumerate(S):
    if s == 'C':
        abc += ab
    if s == 'B':
        ab += a
    if s == 'A':
        a += pow(3, q, MOD)
    if s == '?':
        abc = abc * 3 + ab
        ab = ab * 3 + a
        a = a * 3 + pow(3, q, MOD)
        q += 1
    a %= MOD
    ab %= MOD
    abc %= MOD
    # print(s, a, ab, abc)
print(abc)
