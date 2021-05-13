"""
最大公約数を追い求める。

少なくとも、Aの合計値より答えが大きくなることはない。
なぜなら、どんなに頑張ってもA同士の差分はAの合計値以下になるからである。

答えの最大値はAの合計値。
マイナスを作る必要はない。
0を作る必要はある。

やっぱり、Aの合計値の約数のどれかが答えになりそうだな。証明はできないけど。
Aの合計値の約数を大きいものから順に、実現可能かどうかを検証していけばよい。

"""

from itertools import accumulate

N,K = map(int,input().split())
A = list(map(int,input().split()))
sumA = sum(A)

yakusu = []
d = 1
while d*d < sumA:
    if sumA%d == 0:
        yakusu.append(d)
        yakusu.append(sumA//d)
    d += 1
if d*d == sumA:
    yakusu.append(d)
yakusu.sort(reverse=True)
for d in yakusu:
    #約数の大きい順に、実現可能かどうかを試していく。
    rest = [a%d for a in A]
    rest.sort()
    Rrest = [d-r for r in rest]
    Rrest = Rrest[::-1]
    rest = [0]+list(accumulate(rest))
    Rrest = [0]+list(accumulate(Rrest))
    for i in range(N+1):
        if rest[i] == Rrest[N-i]:
            if rest[i] <= K:
                print(d)
                exit()
            break