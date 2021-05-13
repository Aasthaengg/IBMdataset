S = input()
l = set(S)

res = 10 ** 9
# 使われている文字列を全探索
for x in l:
    # tmp: xでない文字の連続する長さの数え上げ用
    # chk: xでない文字の連続する長さのmax
    tmp, chk = 0, 0
    # 文字列を見ていく
    for s in S:
        # xでない文字の連続する長さのmaxをとっていく
        if s != x:
            tmp += 1
        else:
            chk = max(chk, tmp)
            tmp = 0
    # 文字列の終わり部分
    chk = max(chk, tmp)
    # 連続する長さのmin
    res = min(chk, res)
print(res)