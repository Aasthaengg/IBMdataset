import sys
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7
import math
import statistics
n = I()
xl = LI()

# n人が消費する体力の総和の最小値
# 数直線上にn人が住んでいる
# i番目がXi
# n人全員が参加する集会
# 任意の整数値の座標で集会を開く。座標pで集会を開くときはi番目の人は(Xi-p))**2の体力を消費する。

xl_ceil_mean = math.ceil(statistics.mean(xl))
xl_floor_mean =math.floor(statistics.mean(xl))

sigma_pow1 = sum([(x-xl_ceil_mean)**2 for x in xl])
sigma_pow2 = sum([(x-xl_floor_mean)**2 for x in xl])

if sigma_pow1 > sigma_pow2:
    print(sigma_pow2)
else:
    print(sigma_pow1)