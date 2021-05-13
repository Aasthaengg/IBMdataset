import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

tmp1 = A[0]
for a in A:
    tmp2 = gcd(tmp1, a)
    tmp1 = a * tmp1 // tmp2

ans = 0
for a in A:
    ans += (tmp1 - 1) % a

print (ans)