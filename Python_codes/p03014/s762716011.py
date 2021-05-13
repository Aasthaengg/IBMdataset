def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)
    R = [[0]*W for _ in range(H)]
    L = [[0]*W for _ in range(H)]
    U = [[0]*W for _ in range(H)]
    D = [[0]*W for _ in range(H)]
    for i in range(H):
        cnt1 = 0
        cnt2 = 0
        for j in range(W):
            if S[i][j]=='#':
                cnt1 = 0
            else:
                cnt1 += 1
                L[i][j] = cnt1
        for j in range(W-1, -1, -1):
            if S[i][j]=='#':
                cnt2 = 0
            else:
                cnt2 += 1
                R[i][j] = cnt2

    for j in range(W):
        cnt1 = 0
        cnt2 = 0
        for i in range(H):
            if S[i][j]=='#':
                cnt1 = 0
            else:
                cnt1 += 1
                U[i][j] = cnt1
        for i in range(H-1,-1,-1):
            if S[i][j]=='#':
                cnt2 = 0
            else:
                cnt2 += 1
                D[i][j] = cnt2

    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)
    print(ans)


if __name__ == '__main__':
    main()