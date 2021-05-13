# -*- coding: utf-8 -*-
import sys

N=input()
T=map(int, sys.stdin.readline().split())
A=map(int, sys.stdin.readline().split())

if max(T)!=max(A):
    print 0
    quit()

L=[ None for _ in range(N) ]

#一意に決まる山の高さを配列に代入。配列にNoneで残っているところが山の高さが一意に決まらない箇所
#左から
for i,t in enumerate(T):
    if i==0:
        L[i]=t
    else:
        if prev_t<t:
            L[i]=t
        elif prev_t>t:
            print 0
            quit()
    prev_t=t


#右から
for i,a in enumerate(A[::-1]):
    i=N-i-1 #左から見た順のインデックスに置き換える
    if i==N-1:
        L[i]=a
    else:
        if prev_a<a:
            if L[i] is not None:    #山の高さが既に入っているときは
                if L[i]!=a: #同じ高さじゃないと矛盾があるので、その場合はゼロで終了
                    print 0
                    quit()
            L[i]=a  #それ以外の場合は山の高さを配列に代入
        elif prev_a>a:
            print 0
            quit()
    prev_a=a

#一意に決まる値を入れたLを左から再検査。最大値が配列Aと矛盾していないか
max_x=0
for x,t in zip(L,T):
    #print x,t
    if x is not None:
        max_x=max(max_x,x)
        if max_x!=t:
            print 0
            quit()

#Lを右から再検査
max_x=0
for x,a in zip(L[::-1],A[::-1]):
    if x is not None:
        max_x=max(max_x,x)
        if max_x!=a:
            print 0
            quit()


ans=1
mod=10**9+7
for x,a,t in zip(L,T,A):
    if x is None:   #山の高さがNoneになっている箇所は自由度がある所なので、aとtの最小値の通り数を答えにかける
        ans*=min(a,t)
        ans%=mod
print ans
