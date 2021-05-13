H,W = map(int, input().split())
N = int(input())
A = [int(a) for a in input().split()]

ans = [[-1]*W for _ in range(H)]
i = 0
j = 0
cnt = 0
for k in range(N):
    for _ in range(A[k]):
        if (j == 0 and i%2 == 1) or (j == W-1 and i%2 == 0):
            ans[i][j] = k+1
            cnt += 1
            i += 1
            continue
        if cnt == H*W:
            break
        ans[i][j] = k+1
        cnt += 1
        if i%2 == 0:
            j += 1
        else:
            j -= 1
            
for i in range(H):
    ans[i] = map(str, ans[i])
    print(" ".join(ans[i]))