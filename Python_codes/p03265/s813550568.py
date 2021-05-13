# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

x1, y1, x2, y2 = lr()
P2 = np.array([x2, y2])  # 2つ目の点
A = np.array([[0, -1], [1, 0]])
vec = np.array([x2-x1, y2-y1])
vec2 = np.dot(A, vec)
vec3 = np.dot(A, vec2)
P3 = P2 + vec2
P4 = P3 + vec3
answer = np.concatenate([P3, P4])
print(*answer)
