"""
どんなに操作をおこなっても、全てのi,j(i<j)に関して、Ai,Ajの絶対値の差がsum(A)より大きくなることはない。
したがって、答えがsum(A)より大きくなることはない。
さらに言うなら、数値の状態がワイルドカードである0がベストなので負の値にする必要もない。

また、答えはsum(A)の約数になる。
答えをXとおくと、全ての数はXで割り切れる＝Xの倍数である。
Ai/X = Biとおくと、XBi = Ai　と表すことができる。。
X*sum(B) = sum(A)なので、答えXはsum(A)の約数であることがわかる。

解法：
基本方針としては、sum(A)の約数を列挙して、K回以内の操作で大きい順に実現可能かどうかを調べる。
実現可能かどうかは、各Aiを数が引かれる方と足される方に分けることで考えることができる。
"""
from itertools import accumulate
N,K = map(int,input().split())
A = list(map(int,input().split()))

sumA = sum(A)

#sumAの約数を列挙する。
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
    X = [A[i]%d for i in range(N)]
    X.sort()
    Y = [d-x for x in X]
    Y.sort()
    X = list(accumulate(X))
    Y = list(accumulate(Y))
    Y = Y[::-1]
    for i in range(N-1):
        if X[i] == Y[i+1] and X[i]<=K:
            print(d)
            exit()
    if X[N-1] == 0:
        print(d)
        exit()