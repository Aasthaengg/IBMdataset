s = input()
sa = [i for i in s]
r = 0
for i in range(2**(len(s)-1)):  # 状態数
    si = sa[0]
    for j in range(len(s) - 1):
        t = 2 ** j  # 2^jなので常に2の倍数、
        if i & t:  # どこのビットが1か判定できる 2進数のビット判定を10進数のままやってるイメージ
            si += '+'  # 1なら+を挿入
        si += sa[j+1]
    r += eval(si)  # evalは文の実行なので文字列を都合よく数字に解釈してくれる

print(r)
