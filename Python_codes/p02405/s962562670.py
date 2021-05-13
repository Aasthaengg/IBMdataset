while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    sharp = True
    for i in range(h):
        #奇数行の場合先頭を"#"にする
        if i % 2 != 0:
            sharp = False
        else:
            sharp = True

        #行の出力
        for _ in range(w):
            if (sharp):
                print("#", end="")
                sharp = False
            else:
                print(".", end="")
                sharp = True
        print()
    print()

