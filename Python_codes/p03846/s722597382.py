import sys
sys.setrecursionlimit(10**5)


def pow_mod(n,k,m):#nのk乗したものをmod mしたものを高速に算出する関数
    if k==0:
        return 1
    if k&1:
        return (pow_mod(n,k-1,m)*n%m)%m
    else:
        return (pow_mod(n,k//2,m)**2)%m

N=int(input())
A=list(map(int,input().split()))
MOD=10**9+7
A.sort()

#Nが奇数の場合
#Aをソートして、先頭に0、そのあとは2,2,4,4,となる。そうなっていない場合は間違い


if N&1:
    if A[0]!=0:
        print(0)
        exit()

    for i in range(1,N,2):
        if A[i]!=A[i+1] or A[i]!=i+1:
            print(0)
            exit()
    print(pow_mod(2,((N-1)//2),MOD))

else:
    for i in range(0,N,2):
        if A[i]!=A[i+1] or A[i]!=i+1:
            print(0)
            exit()
    print(pow_mod(2,N//2,MOD))