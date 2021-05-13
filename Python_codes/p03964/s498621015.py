# C - AtCoDeerくんと選挙速報
from math import ceil
n=int(input())
t,a=1,1
for i in range(n):
    tt,aa=map(int,input().split())
    min_num=max(-(-t//tt),-(-a//aa))
    # min_num=max(ceil(t/tt),ceil(a/aa))
    t=min_num*tt
    a=min_num*aa
print(t+a)
