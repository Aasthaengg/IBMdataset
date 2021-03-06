


"""
考察

一点を(0,0におくと)
s / 2 = abs(x1*y2 - x2*y1) / 2
abs(x1*y2 - x2*y1) = s
(x1,y1)になにか入れてみるとして、0を入れると点2のx,yどっちかが消えるので良くない
また、absが邪魔なので、absの一項目を大きくとって、二項目をちいさくとりたい。
ので、10**9 * y2 - x2 = sとする。
s = 10**9 * y2 + x2 ならsを10**9で割った商と余りなのだけども。

s / 10**9 = a あまり bとして、
s / 10**9 = a + 1 あまり +(b-10**9) だから、
y2 = a+1, x2 = 10**9 - b
かな
ただしSが10**9で割り切れるときは x2 = 0
"""

S = int(input())
x0,y0,x1,y1 = 0,0,10**9,1

if S % 10**9 == 0:
    x2, y2 = 0, S // 10**9
else:
    x2, y2 = 10**9 - (S % 10**9), S // 10**9 + 1

print(x0,y0,x1,y1,x2,y2)