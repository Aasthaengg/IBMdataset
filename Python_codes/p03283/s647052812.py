import numpy as np
import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
cnt = np.zeros((n+1, n+1), dtype=np.int32)
L, R = map(np.array, zip(*[map(int, input().split()) for _ in range(m)]))
np.add.at(cnt, (L, R), 1)

S = np.cumsum(cnt, axis=0).cumsum(axis=1)
L, R = map(np.array, zip(*[map(int, input().split()) for _ in range(q)]))

ans = S[R, R]-S[R, L-1]-S[L-1, R]+S[L-1, L-1]
print(*ans, sep='\n')