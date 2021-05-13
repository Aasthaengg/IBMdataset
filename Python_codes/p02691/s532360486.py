'''
i<j としたとき求めたいのは
i + Ai = j - Aj の組み合わせの数
そこで各々の Li = i + Ai, Ri = i - Aiを計算し辞書型で保持しておく
'''
from collections import defaultdict

N =int(input())
A = list(map(int,input().split()))
Li = defaultdict(int)
Ri = defaultdict(int)
for i,a in enumerate(A,start=1):
    Li[i+a] += 1
    Ri[i-a] += 1

ans = 0
for k,v in Li.items():
    if k in Ri:
        ans += Li[k]*Ri[k]

print(ans)