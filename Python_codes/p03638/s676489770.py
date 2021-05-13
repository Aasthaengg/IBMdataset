H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
A = []
for i in range(len(a)):
    A += [i + 1] * a[i]

ans = [[0] * W for _ in range(H)]

for i in range(len(A)):
    h = i // W
    w = i % W
    if h % 2 == 0:
        ans[h][w] = A[i]
    else:
        ans[h][W - w - 1] = A[i]


for i in range(H):
    print(*ans[i])
