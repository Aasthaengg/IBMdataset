
def resolve():
    H, W = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(H)]

    ans = []
    # 横走査
    for i in range(H):
        for j in range(W - 1):
            if AB[i][j] % 2:
                AB[i][j] -= 1
                AB[i][j + 1] += 1
                ans.append((i, j, i, j + 1))

    # 最後の列を走査
    for i in range(H - 1):
        if AB[i][W - 1] % 2:
            AB[i][W - 1] -= 1
            AB[i + 1][W - 1] += 1
            ans.append((i, W - 1, i + 1, W - 1))

    print(len(ans))
    for (a, b, c, d) in ans:
        print(a + 1, b + 1, c + 1, d + 1)


if __name__ == "__main__":
    resolve()