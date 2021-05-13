# サンプル3
# 6
# 6 5 4 3 2 1
# b=3で2+0+2+4+6+8 = 22 b=4で1+1+3+5+7+9=26
# わからんからコード書いて試す
n = int(input())
a = list(map(int, input().split()))
# for b in range(-10, 10):
#     tmp = 0
#     for i, v in enumerate(a):
#         tmp += abs(v - (b + i + 1))
#     print(f"b={b}, tmp={tmp}")
# でかくても小さくてもダメっぽい
# 三分探索？やったことないしやり方わからんからググる
# めぐる式にこれhttps://qiita.com/ganariya/items/1553ff2bf8d6d7789127をしただけ

ok, ng = -10**9, 10**9 + 1


def calc(b):
    ret = 0
    for i, v in enumerate(a):
        ret += abs(v - (b + i + 1))
    return ret


# なぜかTLEなるのでカウンタを設置してみた
c = 0
while c < 100:
    c += 1
    c1 = (2 * ok + ng) // 3
    c2 = (ok + 2 * ng) // 3
    b1, b2 = calc(c1), calc(c2)
    if b1 > b2:
        ok = c1 + 1  # +1のきもちは不明
    else:
        ng = c2

print(calc(ok))
