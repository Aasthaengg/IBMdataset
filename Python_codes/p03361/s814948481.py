H, W = map(int, input().split())

S = [input() for _ in range(H)]

jdg = True
for i in range(H):
    for j in range(W):
        ans = 0
        if S[i][j] == '#':
            ans += 1
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= i + y <= H - 1 and 0 <= j + x <= W - 1:
                    if S[i + y][j + x] == '#':
                        ans += 1
            if ans == 1:
                jdg = False
                break
    if not jdg:break
print('Yes' if jdg else 'No')