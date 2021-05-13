#全国統一プログラミング王決定戦予選-C Different Strokes
"""
問題を言い換えた時に、
高橋くんがa+bの幸福度を得られる時に、
青木さんが-a-bの妨害をできる
と言い換えても、最適な行動が取れる。
よって、a+bの降順にソートして、
高橋くんの番なら+a
青木さんの番なら-b
することで答えが得られる
"""
import sys
from operator import itemgetter
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
AB = []
for i in range(n):
    a,b = map(int,readline().split())
    AB.append([a+b,a,b])

AB.sort(reverse=True)

ans = 0
for i in range(n):
    if even(i):
        ans += AB[i][1]
    else:
        ans -= AB[i][2]

print(ans)