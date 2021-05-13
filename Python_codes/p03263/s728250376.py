# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W = lr()
A = [lr() for _ in range(H)]
answer = []
for i in range(H):
    for j in range(W-1):
        if A[i][j]&1:
            answer.append((i+1, j+1, i+1, j+2))
            A[i][j+1] += 1

for i in range(H-1):
    if A[i][-1]&1:
        answer.append((i+1, W, i+2, W))
        A[i+1][-1] += 1

print(len(answer))
print('\n'.join('{} {} {} {}'.format(a, b, c, d) for a, b, c, d in answer))
