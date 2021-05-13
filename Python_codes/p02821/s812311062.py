import sys
from bisect import bisect_left, bisect_right
import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
#print("A={}".format(A))
"""
この問題の前半は、合計の幸福度Xが上位M個未満に入るかを判定する。
    -> Xに関する二分探索をすることで、上位から丁度M番目の幸福度がわかる！

これを判定するために、左手の握手先をfix(A[i]とする)して、
右手の幸福度が(X - A[i])以上であるものの個数を数える。
"""

def within(X, M):
    """
    幸福度がX以上上がるような握手の組がM個未満ならTrue、そうでなければFalseを返す
    """
    pair = 0
    for i in range(N):
        idx = bisect_left(A, X - A[i])
        pair += N - idx
    if pair < M:
        #print("pair={}<M".format(pair))
        return True
    else:
        #print("pair={}>=M".format(pair))
        return False

"""
Xに関する二分探索をおこなった結果、
leftXはwithin(leftX, M) == Trueになる最小のX
"""
leftX = 0
rightX = A[-1] * 2 + 1
while leftX != rightX:
    middleX = (leftX + rightX) // 2
    #print("mid={}".format(middleX))
    if within(middleX, M):
        rightX = middleX
    else:
        leftX = middleX + 1
#print("leftX={}".format(leftX))

"""
これより後半、幸福度の総和を求める。
前半同様に左手をfixした上で、両手の幸福度の合計がleftX以上になるときの幸福度を加算していく。
単純に右手に関してfor文を回して加算するとTLEなので、
右手の幸福度に関しては先に累積和を求めておく。
"""
S = list(itertools.accumulate(A))
#print("S={}".format(S))
happy = 0
times = 0
for i in range(N):
    idx = bisect_left(A, leftX - A[i])
    times += N - idx
    #print("When i={}, idx={}, times={}".format(i, idx, times))
    if idx != 0:
        happy += A[i] * (N - idx) + (S[-1] - S[idx - 1])
    else:
        happy += A[i] * (N - idx) + S[-1]
    #print("happy={}".format(happy))
happy += (leftX - 1) * (M - times)

print(happy)
