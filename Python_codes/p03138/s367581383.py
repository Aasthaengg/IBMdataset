# -*- coding: utf-8 -*-
N,K=map(int, raw_input().split())
A=map(int, raw_input().split())

#10**12は2進数で40桁あるので、余裕を見て50桁分用意しておく
keta=50
L=[[N,0]]
#a1~anの同じ桁を見て、0の出現個数、1の出現個数を数える
for i in range(keta-1,-1,-1): #i 何桁目を見ているかを表す
    count=[ 0 for _ in range(2) ]
    for a in A:
        key=a>>i&1  #key aを2進数で表現した時、i桁目が0か1かをkeyに代入
        count[key]+=1
    L.append(count)

T=[ float("-inf") for _ in range(keta+1) ]
F=[ float("-inf")  for _ in range(keta+1) ]
F[0]=0

for i in range(1,keta+1):
    bit=K>>(keta-i)&1
    if bit==1:
        F[i]=F[i-1]+2**(keta-i)*L[i][0] #未満:Falseのdp表の横向き（→）の遷移
        #max( 未満:False→未満：Trueへのdp表の斜めの遷移、 未満:Falseのdp表の横向き（→）の遷移 bitが1、未満:Falseのdp表の横向き（→）の遷移 bitが0 )
        T[i]=max( F[i-1]+2**(keta-i)*L[i][1],T[i-1]+2**(keta-i)*L[i][0],T[i-1]+2**(keta-i)*L[i][1] )
    else:
        F[i]=F[i-1]+2**(keta-i)*L[i][1] #未満:Falseのdp表の横向き（→）の遷移
        T[i]=max( T[i-1]+2**(keta-i)*L[i][0],T[i-1]+2**(keta-i)*L[i][1] )   #未満:Trueのdp表の横向き（→）の遷移


print max(T[-1],F[-1])
