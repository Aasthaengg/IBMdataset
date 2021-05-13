# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


A, B, K = LI()

player = 0
for i in range(K):
    if player == 0:
        if A % 2 == 1:
            A -= 1
        B += A // 2
        A //= 2
    else:
        if B % 2 == 1:
            B -= 1
        A += B // 2
        B //= 2
    player ^= 1

print(A, B)
