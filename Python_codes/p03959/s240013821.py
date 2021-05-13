#CODE FESTIVAL 2016 qual C-C 二人のアルピニスト
"""
左右一列に並んでいる山を、左右から見ていった時に今まで見た中の最大値が分かる。
この状態で、山の高さの列が何通りあるか求めよ。

単純に、山の高さの"幅"を求めて、その分だけかけ合わせれば良さそう。

辻褄が合わないのは
1.高さが確定している場所同士で、辻褄が合わない
2.片方の高さが確定している場所で、もう片方の値がそれより小さい
このとき0
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
L = list(map(int,readline().split()))
R = list(map(int,readline().split()))
mod = 10**9 + 7

mx = 0
L1 = []
for i in range(n):
    if mx < L[i]:
        L1.append((1,L[i]))
        mx = L[i]
    else:
        L1.append((0,L[i]))

R1 = []
mx = 0
for i in range(n-1,-1,-1):
    if mx < R[i]:
        R1.append((1,R[i]))
        mx = R[i]
    else:
        R1.append((0,R[i]))
R1.reverse()
ans = 1
for i in range(n):
    if L1[i][0] == 1:
        if R1[i][0] == 1:
            if L1[i][1] != R1[i][1]:
                ans = 0
                break
        else:
            if L1[i][1] > R1[i][1]:
                ans = 0
                break
    elif R1[i][0] == 1:
        if R1[i][1] > L1[i][1]:
            ans = 0
            break
    else:
        ans *= min(L1[i][1],R1[i][1])
        ans %= mod

print(ans)