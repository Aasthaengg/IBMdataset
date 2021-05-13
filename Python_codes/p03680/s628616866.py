def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    lst = [False] * N
    i = 1  # 光っているボタン
    cnt = 0
    flag = False

    for _ in range(N):
        lst[i - 1] = True  # 今光っているボタンを記録
        cnt += 1  # 今光っているボタンを押す
        i = a[i - 1]  # 新しく光るボタン

        if i == 2:  # ボタン2が光ったら終了
            flag = True
            break

        if lst[i - 1] == True:  # 新しく光るボタンが過去に光ったことがある
            flag = False
            break

    if flag == True:
        print(cnt)
    else:
        print(-1)


if __name__ == "__main__":
    main()
