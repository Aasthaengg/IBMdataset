import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

from bisect import bisect_left


def combination(n, r): #nCrを求める
    if n - r < r:
        r = n - r
    tmp = 1
    for i in range(n - r + 1, n + 1):
        tmp *= i
    for i in range(1, r + 1):
        tmp //= i
    return tmp



N = int(input())
A = list(map(int, input().split()))
A.sort()

a1 = A[-1]
tmp = bisect_left(A, a1 // 2)
b1 = A[tmp]

if tmp != 0:
    if abs(b1 / a1 - 1/2) >= abs(A[tmp - 1] / a1 - 1/2):
        b1 = A[tmp - 1]

print (a1, b1)