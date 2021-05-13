# coding: utf-8

import sys
import math
import collections
import itertools
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def lcm(x, y) : return (x * y) // math.gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def LS() : return input().split()
def RS(N) : return [input() for _ in range(N)]
def LRS(N) : return [input().split() for _ in range(N)]
def PL(L) : print(*L, sep="\n")
def YesNo(B) : print("Yes" if B else "No")
def YESNO(B) : print("YES" if B else "NO")

N, K = LI()
S = input()

nums = []
now = 1
cnt = 0
for s in S:
    if s == str(now):
        cnt += 1
    else:
        now = 1 - now
        nums.append(cnt)
        cnt = 1
if cnt != 0:
    nums.append(cnt)
if now == 0:
    nums.append(0)

C = [0] * (len(nums)+1)
for i in range(len(nums)):
    C[i+1] = C[i] + nums[i]

ans = 0
m = 2 * K + 1
for i in range(0, max(len(nums)-m+1, 1), 2):
    m = min(m, len(nums))
    ans = max(ans, C[i+m] - C[i])

if len(nums) != 1:
    print(ans)
else:
    print(nums[0])
