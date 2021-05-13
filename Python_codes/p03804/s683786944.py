# coding: utf-8
N,M=map(int,input().split())
picN=[]
picM=[]

for i in range(N):
    L=list(input())
    picN.append(L)

for i in range(M):
    L=list(input())
    picM.append(L)

K=N-M

for i in range(K+1):
    for j in range(K+1):
        flg=True
        for a in range(M):
            for b in range(M):
                if picN[a+i][b+j]!=picM[a][b]:
                    flg=False
        if flg:
            break
    if flg:
        break

if flg:
    print("Yes")
else:
    print("No")