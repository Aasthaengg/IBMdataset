"""
実際にN!を計算するわけには行かない。
memo[n] => nの素因数分解の結果

sum(memo[N])の素因数分解の結果から
"""
from collections import Counter
N = int(input())
memo = [None]*(N+1)

for i in range(2,N+1):
    tmp = []
    n = i
    d = 2
    while n!=1:
        while n%d==0:
            tmp.append(d)
            n//=d
        d += 1
    memo[i] = Counter(tmp)

count = Counter([])
for i in range(2,N+1):
    count += memo[i]

ans = 0
#数が74個以上ある素因数の数
c74 = 0
#数が24個以上ある素因数の数
c24 = 0
#数が14個以上ある素因数の数
c14 = 0
#数が4個以上ある素因数の数
c4 = 0
#数が2個以上ある素因数の数
c2 = 0

for v in count.values():
    if v >= 2:
        c2 += 1
    if v >= 4:
        c4 += 1
    if v >= 14:
        c14 += 1
    if v >= 24:
        c24 += 1
    if v >= 74:
        c74 += 1

ans += c74
ans += c24 * (c2-1)
ans += (c4*(c4-1))//2 * (c2-2)
ans += c14 * (c4-1)


"""
#1つの素因数で75数を形成できるパターンをみつける
for k,v in count.items():
    if v >= 74:
        ans += 1
    
#2つの素因数(a,b)で3,25のパターンで、75数を形成できるパターンを見つける
for k,v in count.items():
    if v >= 24:
        for k2,v2 in count.items():
            if k2 != k and v2 >= 2:
                ans += 1

#2つの素因数(a,b)で5,15のパターンで、75数を形成できるパターンを見つける
for k,v in count.items():
    if v >= 14:
        for k2,v2 in count.items():
            if k2 != k and v2 >= 4:
                ans += 1

#2つの素因数(a,b)で3,25のパターンで、75数を形成できるパターンを見つける
for k,v in count.items():
    if v >= 4:
        for k2,v2 in count.items():
            if k2 != k and v2 >= 4:
                for k3,v3 in count.items():
                    if k3 != k and k3!=k2 and v3 >= 2:
                        ans += 1
"""

print(ans)

