import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

from fractions import gcd

A, B = map(int, input().split())

print (A * B // gcd(A, B))