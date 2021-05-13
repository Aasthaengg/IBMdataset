"""
成績をSにできるか？という二分探索をするのがよさそう。
S秒以内に全員が食べ終わった状態でいる必要がある。
S/xをすることで、各メンバーのキャパシティが見えてくる。
あとは「食べ物をどう割り当てるか」だけどこれは貪欲的にキャパシティの小さい順に、食べづらさの小さい食べ物を割り当てればOK。
もし、キャパシティが足りない場合はK回までxを調整して、キャパシティを計算しなおす。
計算量としては、O(log(10**12)N)で間に合う。

"""

N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort(reverse=True)
F.sort()
from math import ceil

def is_ok(S):
    tmpK = K
    for i in range(N):
        f = F[i]
        a = A[i]
        if S//a < f:
            x = ceil(a-S/f)
            tmpK -= x
        if tmpK < 0:
            return False
    return True

def bisearch(high,low):
    while high - low > 1:
        mid = (high+low)//2
        if is_ok(mid):
            high = mid
        else:
            low = mid
    return high

print(bisearch(max(A)*max(F),-1))