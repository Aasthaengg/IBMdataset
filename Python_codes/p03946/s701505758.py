# -*- coding: utf-8 -*-
import sys 
from collections import deque
from collections import defaultdict
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, T = map(int, readline().split())
A = list(map(int,readline().split()))

### セグメント木
# 0-index
# N: 処理する区間の長さ
N0 = 2**(N-1).bit_length()
data = [0]*(2*N0)

# 初期化
def init(A):
    for i in range(N):
        data[i+N0-1] = A[i]
    for i in range(N0-2,-1,-1):
        data[i] = max(data[2*i+1],data[2*i+2])

# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = max(data[2*k+1], data[2*k+2])

# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])

        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

init(A)
d = defaultdict(int)
for i in range(N-1):
    a = A[i]
    high = query(i+1,N+1)
    p = high - a
    d[p] += 1
d = sorted(d.items(),reverse=True)
print(d[0][1])