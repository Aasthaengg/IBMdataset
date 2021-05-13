H, W = map(int, input().split())
N = int(input())
arr = list(map(int, input().split()))
ans = [[0]*W for _ in range(H)]
count = 0
index = 0
for h in range(H):
    for w in range(W):
        if h % 2 == 0:
            ans[h][w] = index + 1
        else:
            ans[h][W-1-w] = index + 1
        count += 1
        if count == arr[index]:
            count = 0
            index += 1
for h in range(H):
    for w in range(W):
        print(ans[h][w], end=" ")
    print()