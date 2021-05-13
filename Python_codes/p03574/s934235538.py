def resolve():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        s = input()
        S.append(s)
    for i in range(H):
        ans = ""
        for j in range(W):
            count = 0
            if S[i][j] == "#":
                ans += "#"
            else:
                if i >= 1 and j >= 1:
                    if S[i-1][j-1] == "#":
                        count += 1
                if i >= 1:
                    if S[i-1][j] == "#":
                        count += 1
                if i >= 1 and j <= W-2:
                    if S[i-1][j+1] == "#":
                        count += 1
                if j >= 1:
                    if S[i][j-1] == "#":
                        count += 1
                if j <= W-2:
                    if S[i][j+1] == "#":
                        count += 1
                if j >= 1 and i <= H-2:
                    if S[i+1][j-1] == "#":
                        count += 1
                if i <= H-2:
                    if S[i+1][j] == "#":
                        count += 1
                if i <= H-2 and j <= W-2:
                    if S[i+1][j+1] == "#":
                        count += 1
                ans += str(count)
        print(ans)
resolve()