def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    
    left = [[-1]*W for _ in range(H)]
    right = [[-1]*W for _ in range(H)]
    up = [[-1]*W for _ in range(H)]
    down = [[-1]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                if j == 0:
                    left[i][j] = 0
                else:
                    left[i][j] = left[i][j-1] + 1
                if i == 0:
                    up[i][j] = 0
                else:
                    up[i][j] = up[i-1][j] + 1

            if S[-1-i][-1-j] == '.':
                if j == 0:
                    right[-1-i][-1-j] = 0
                else:
                    right[-1-i][-1-j] = right[-1-i][-1-(j-1)] + 1
                if i == 0:
                    down[-1-i][-1-j] = 0
                else:
                    down[-1-i][-1-j] = down[-1-(i-1)][-1-j] + 1

    ans = 0
    temp = [0] * W
    for i in range(H):
        for j in range(W):
            temp[j] = left[i][j] + right[i][j] + down[i][j] + up[i][j] + 1
        ans = max(ans, max(temp))
    print(ans)

main()