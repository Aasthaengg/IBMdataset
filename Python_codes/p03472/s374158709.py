#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, H = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

max_a = max(A)
B.sort(reverse=True)

# is_OK(x) を x 回の攻撃で H ポイント与えられれば1, そうでなければ0を返す関数とする
# 二分探索


def is_OK(x):
    count = 0
    damage = 0
    for n in range(N):
        if B[n] > max_a and count < x:
            count += 1
            damage += B[n]
    damage += (x-count) * max_a
    if H - damage <= 0:
        return True
    else:
        return False


ng, ok = 0, 10**9+1
while ok - ng > 1:
    mid = ng + (ok - ng) // 2
    if is_OK(mid):
        ok = mid
    else:
        ng = mid

print(ok)
