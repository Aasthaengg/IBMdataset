H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ans = [[0] * W for _ in range(H)]
flg = 0
i = 0
for h in range(H):
    flg ^= 1
    if flg:
        w_list = list(range(W))
    else:
        w_list = reversed(list(range(W)))
    for w in w_list:
        if A[i]:
            ans[h][w] = i+1
            A[i] -= 1
        else:
            i += 1
            ans[h][w] = i+1
            A[i] -= 1
for h in range(H):
    print(*ans[h])
