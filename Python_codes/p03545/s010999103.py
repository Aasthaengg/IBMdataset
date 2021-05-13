# ABC079 C
abcd = input()
ABCD = []
for i in range(len(abcd)):
    ABCD.append(abcd[i])

# print(ABCD)

# 全通り検査する
for i in range(2**3):
    op = []

    # 各ビットのチェック
    for j in range(3):
        # 最下位ビットが１なら"+"
        if ((i >> j) & 1):
            op.append("+")
        else:
            op.append("-")
    # 全パターン網羅できていること確認
    # print(op)

    # ans = 0
    # for k in range(len(op)):
    #     if op[k] == "+":
    #         ans = ABCD[k]+ABCD[k+1]
    #         ABCD[k+1] = ans
    #         print(ans)
    #     else:
    #         ans = ABCD[k]-ABCD[k+1]
    #         ABCD[k+1] = ans
    # if ans == 7:
    #     print(op)

    # 数値の配列と演算子の配列の結合
    tmp = [None] * (len(ABCD)+len(op))
    # 最初から最後まで1個飛ばしで代入
    tmp[::2] = ABCD
    tmp[1::2] = op
    # print(tmp) # 色の配列完成
    
    # 計算
    ans = ""
    for i in tmp:
        ans += i
    # evalは文字列をpythonのコードとして実行してくれる関数，つまり文字列で表現された数式を計算してくれる
    if eval(ans) == 7:
        print(ans + "=7")
        exit()

