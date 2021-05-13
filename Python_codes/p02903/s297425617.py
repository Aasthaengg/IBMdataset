import sys
readline = sys.stdin.readline
H, W, B, A = map(int, readline().split())

S = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if not ((i < A) ^ (j < B)):
            S[i][j] = 1
print('\n'.join([''.join(map(str, a)) for a in S]))
