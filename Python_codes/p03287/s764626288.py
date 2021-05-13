# coding: utf-8

n,m = list(map(int,input().split()))
A = list(map(int,input().split()))

#（↓）累積和を別のリストに格納する必要はなく、
# modmという変数を1つ用意して、modmにその時点での
# 累積和のmod mを格納すればよい
modm = 0

#（↓）{x:y}:Aの各要素を順に処理していくとき、
# mod mがxである要素が現時点までにy個見つかっていることを表す
dic = {0:1}

cnt = 0
for a in A:
    modm = (modm+a) %m
    cnt += dic.get(modm,0)
    dic[modm] = dic.get(modm,0) + 1
#（↑）c[b]では、bをキーとする要素が見つからなかった場合
# エラーが発生してしまう。
#（↑）c.get(b,default)なら、bをキーとする要素が見つからなかった場合
# デフォルト値を返してくれる。

print(cnt)