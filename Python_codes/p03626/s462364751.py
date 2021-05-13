N = int(input())
s = input()
c = input()

#データの加工
d = 0 #d=1:横向き, d=0:縦向き
domino = []
pre = s[0]
s += '_'
for x in s[1:]:
    if x == pre:
        d += 1
    else:
        domino.append(d)
        d = 0
    pre = x

#初期値（最初のドミノが横向きか縦向きか）
if domino[0] == 1: ans = 6
else: ans = 3

prex = domino[0]
for x in domino[1:]:
    if prex == 0: ans *= 2
    elif x == 1: ans *= 3
    #elif x == 0: ans *= 1
    prex = x
ans %= 1000000007
print(ans)