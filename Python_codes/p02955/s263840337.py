"""
まず、答えは必ずAの総和以下になる。なぜなら、A同士の差の最大値がAの総和だからである。
移動回数が足りるのであれば、一つだけAの総和になるような項を作って、他を全部0にするのがよい。
ここからわかるのは、数を移動させ終わった後の各Aは全て0以上になるということである。

また答えはからなずAの総和の約数になる。
理由：
答えをXとすると、各AはbXと表すことができる。
したがって、Aの総和＝(bの総和*X)となる。
ゆえに、答えXはAの総和の約数である。

解法としては、Aの総和の約数を列挙して、大きい順に実現可能かどうかを試していく。
実現可能かどうかを試すには、各Aを総和の約数dで割ったときの余りをもとめて、小さい順にソートする。
そのうえで、左からL番目までを「数を与える側」、L+1番目以降を「数をもらう側」として余りが0になるように調整できないかを確かめる。
これは累積和を活用することですくない計算量で実行可能である。
最後に、移動した数がK以下かどうかを確認する。
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