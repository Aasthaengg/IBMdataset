#ABC105-D Candy Distribution
"""
al~arの合計がmの倍数となる通り数を調べる。
愚直に累積和をとって判定するには、O(n(n+1)/2)で不十分
実は、al~arの合計がmの倍数になる条件は、累積和をbとして、
b(l-1),brのmod m が同値になることである。
よって、累積和のmod mの個数をdictで保存しておいて、
同じ値のnC2つまり、n(n-1)//2の合計が答えとなる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m = map(int,readline().split())
lst1 = list(map(int,readline().split()))
def cumsum(lst): #元のリストを保持
    res = lst[:]
    for i in range(1,len(res)):
        res[i] += res[i-1]
    return res
lst2 = cumsum(lst1)

dic1 = dict()
for i in lst2:
    res = i%m
    if res in dic1:
        dic1[res] += 1
    else:
        dic1[res] = 1

ans = 0
for i in dic1.values():
    if i >= 2:
        ans += i*(i-1)//2

res = 0 if 0 not in dic1 else dic1[0]
print(ans+res)
