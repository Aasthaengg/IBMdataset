H, W = map(int, input().split())
S = [input() for _ in range(H)]
Ans = [[[-1, -1]for __ in range(W)] for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        else:
            if Ans[i-1][j][0] != -1:
                Ans[i][j][0] = Ans[i-1][j][0]
            else:
                num0 = 0
                while True:
                    num0 += 1
                    if i + num0 >= H:
                        break
                    elif S[i+num0][j] == '#':
                        break
                Ans[i][j][0] = num0

            if Ans[i][j-1][1] != -1:
                Ans[i][j][1] = Ans[i][j-1][1]
            else:
                num1 = 0
                while True:
                    num1 += 1
                    if j + num1 >= W:
                        break
                    elif S[i][j+num1] == '#':
                        break
                Ans[i][j][1] = num1

        ans = max(ans, sum(Ans[i][j]))
print(ans-1)
