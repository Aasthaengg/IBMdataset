def abc105_c():
    n = int(input())
    # 例外処理
    if n == 0:
        print(0)
        return

    # dを超えない数の商と、余りをとる
    d = n
    bin_arr = []
    while d != 0:
        # dが正の値なら、dを超えない数は、絶対値は小さいほう
        if d > 0:
            _d = d // 2
            bin_arr.append(d % 2)
            d = -1 * _d  # さいごに-1掛ける
        # dが負の値なら、dを超えない数は、絶対値としては大きいほう
        else:
            _d = (abs(d) + 1) // 2
            bin_arr.append(abs(d) % 2)
            d = _d
        #print(d, bin_arr)

    bin_str = ''.join(map(str, reversed(bin_arr)))
    print(bin_str)

abc105_c()