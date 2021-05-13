s = input()
lens = len(s)
# パーとグーを置換すると、その前後でスコアは変わらない
# ggの時,pgとgpの点数はともに1
# gpの時,pgとgpの点数はともに0 って感じ
#ので、パーをばらけさせても後ろに固めても回数が同じなら結果は同じ -> AtcoDeerくんがパーを出せる回数 - TopcoDeerくんがパーを出した回数が答え
numpar = lens // 2
toppar = 0
for i in range(lens):
    if s[i] == "p":
        toppar += 1
print(str(numpar - toppar))