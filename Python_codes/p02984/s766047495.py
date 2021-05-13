#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

# 2* x_0 = A[0] + A[N-1] + (A[2] + A[4] + ... (偶数項) ) - (A[1] + A[3] + ... (奇数項))
# あとは順次x_1, x_2, を求めていけば良い

even = 0
odd = 0
for i in range(N):
    if i % 2:
        odd += A[i]
    else:
        even += A[i]

X = [0] * N
X[0] = even - odd

for i in range(1, N):
    X[i] = 2*(A[i-1] - X[i-1]//2)

X = [str(x) for x in X]
print(" ".join(map(str, X)))


