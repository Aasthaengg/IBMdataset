def solve(H, W, s):
    scores = [[float('inf') for _ in range(W)] for _ in range(H)]
    scores[0][0] = 0 if s[0][0] == '.' else 1

    for i in range(H):
        for j in range(W):
            for x, y in [(i - 1, j), (i, j - 1)]:
                if x < 0 or y < 0:
                    continue
                if s[i][j] == '.' or s[x][y] == '#':
                    scores[i][j] = min(scores[i][j], scores[x][y])
                else:
                    scores[i][j] = min(scores[i][j], scores[x][y] + 1)

    return scores[H - 1][W - 1]

if __name__ == '__main__':
    H, W = map(int, input().split())
    s = []
    for _ in range(H):
        s.append(list(input()))

    print(solve(H, W, s))
