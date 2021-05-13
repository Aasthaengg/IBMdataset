import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

a, b, c = map(int, input().split())

if (b - a == c - b):
    print ('YES')
else:
    print ('NO')