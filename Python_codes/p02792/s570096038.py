
def resolve():
    N = int(input())
    # cnt[i][j] := 先頭がi, 末尾がjで始まるような数
    cnt = [[0] * 10 for i in range(10)]
    for i in range(1, N + 1):
        a = int(str(i)[0])  # 先頭
        b = int(str(i)[-1])  # 末尾
        cnt[a][b] += 1

    ans = 0
    for i in range(10):
        for j in range(10):
            ans += cnt[i][j] * cnt[j][i]
    print(ans)


if __name__ == "__main__":
    resolve()
