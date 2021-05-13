def sumitrust2019_d_01():
    n = int(input())
    s = input()
    ans = 0

    for i in range(1000):
        # 確認するpinの数字の組み合わせと桁の初期化
        # pin = list(str(i).zfill(3))
        pin = f'{i:0>3}'

        # list+indexで書こうと思ったけど、そもそも文字列でやっているのでfindで探しちゃう
        p1 = s.find(pin[0])

        if p1 != -1:
            p2 = s.find(pin[1], p1 + 1)
            if p2 != -1:
                p3 = s.find(pin[2], p2 + 1)
                if p3 != -1:
                    ans += 1

    print(ans)

if __name__ == '__main__':
    sumitrust2019_d_01()