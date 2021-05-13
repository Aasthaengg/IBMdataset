H,W,A,B=map(int,input().split())
ans = [['0'] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if x < A and y < B:
            ans[y][x] = '1'
        elif x >= A and y >= B:
            ans[y][x] = '1'
for a in ans:
    print(''.join(a))