#AGC019-B Reverse and Compare
"""
全通りのスワップから、重複する要素を引くことで求まる。
(解説では、この逆で貪欲に重複しない要素を数え上げる解法だが、本質的には同じ)

1.Ai==Ajとなる添字を選んだとき、その結果は
A[i+1:j]の結果と等しくなるのでこれを省く。

2.Ai!=Ajとなる添字を選んだとき、必ずそれと重複するようなスワップの方法、また
スワップをしなかった場合とは異なるものになる。

よって、答えは全通りからi<jとなるAi,Ajに対して、Ai==Ajの個数を引いた数になる。
つまり、文字列の長さをnとしたとき、まず全通りは
ans = nC2
で表され、
ここからi<jとなるi,jにおいて、Ai==Ajとなる文だけ引く。
このとき、Kという事前に準備した配列を用いているが、
各アルファベットの出現回数について、一括で重複回数を求められるようにしてある。
"""
import sys
from collections import defaultdict
dic1 = defaultdict(int)
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')
n = len(s)

#二項係数(modなし) O(k)
def large_conbination(n,k): #no mod. return nCk.
    res1 = 1
    for i in range(n,n-k,-1):
        res1*=i
    res2 = 1
    for i in range(1,k+1):
        res2*= i
    return res1//res2

ans = large_conbination(n,2)

for i in s:
    dic1[i] += 1

K = [0]
for i in range(2*(10**5)):
    K.append(K[-1]+(i+1))

for i in dic1.values():
    if i < 2:
        continue
    ans -= K[i-1]

print(ans+1)
