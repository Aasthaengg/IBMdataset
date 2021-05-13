from collections import Counter
from math import factorial

def comb(n,r):
    return factorial(n)//factorial(r)//factorial(n-r)

N,A,B = map(int,input().split())
V=list(map(int,input().split()))

V_C=Counter(V)

max_val=max(V)
CC=V_C[max_val]
if A<=CC:
    ans=0
    for v in range(A,min(B,CC)+1):
        ans+=comb(CC,v)
    print(max_val)
    print(ans)
    exit()

tmp_sum=0
tmp_num=0

for key in sorted(V_C.keys(),reverse=True):
    val = V_C[key]
    assert tmp_num<A
    #追加しても大丈夫なら加える(加えないとAに行かないから加えないといけない)
    #ぎりAに届くように追加するのが良い
    if A<=tmp_num+val:
        rest=A-tmp_num

        tmp_num+=rest
        tmp_sum+=key*rest
        assert tmp_num==A
        assert rest<=val
        assert rest!=0
        print(tmp_sum/tmp_num)
        print(comb(val,rest))
        exit()
    else:
        tmp_num+=val
        tmp_sum+=key*val
        assert tmp_num<A

assert 1==2
