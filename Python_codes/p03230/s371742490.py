# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


N = I()

x = -1
for i in range(500):
    if N == i * (i + 1) // 2:
        x = i

if x == -1:
    print('No')
    exit()

print('Yes')
print(x + 1)
num = [i + 1 for i in range(N)]
S = [[0] * x for _ in range(x + 1)]
k = 0
for i in range(x):
    for j in range(i, x):
        S[i][j] = num[k]
        S[j + 1][i] = num[k]
        k += 1

for s in S:
    print(len(s), ' '.join(map(str, s)))
