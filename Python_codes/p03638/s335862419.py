import sys
input = sys.stdin.readline

H, W = [int(x) for x in input().split()]
N = int(input())
a = [int(x) for x in input().split()]
A = []
for i in range(N):
    A += [str(i + 1)] * a[i]

ans = [["0"] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans[i][j] = A.pop(0)

for i in range(H):
    if i % 2 == 0:
        print(*ans[i])
    else:
        print(*ans[i][::-1])
