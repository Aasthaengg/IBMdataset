S = input()
K = int(input())
s = list(map(int, list(S)))

if K <= 100:
    # 1からK文字目まで連続した1が見つかるかを探す
    for i in range(K):
        if s[i] != 1:
            # 1ではない -> つまりこの数字
            print(S[i])
            break
    else:
        # 1が連続している -> 1
        print(1)
else:
    # 一番最初に発見した1以外の数字
    for c in s:
        if c != 1:
            print(c)
            break
