import math, sys

H,W,K = list(map(int, input().split()))

map=[]
Hs=[]
Ws=[]
for _ in range(H):
    row=list(input())
    map.append(row)
    Hs.append(row.count("#"))
for i in range(W):
    count=0
    for j in range(H):
        if map[j][i]=="#":
            count+=1
    Ws.append(count)
#print(Hs,Ws)
tot = sum(Hs)
ans=0
for i in range(2**H):
    for j in range(2**W):
        i_bin=(bin(i)[2:]).zfill(H)
        j_bin=(bin(j)[2:]).zfill(W)
        count=0
        for i2 in range(H):
            if i_bin[i2]=="1":
                count+=Hs[i2]
        for j2 in range(W):
            if j_bin[j2]=="1":
                count+=Ws[j2]
        for i2 in range(H):
            for j2 in range(W):
                if i_bin[i2]=="1" and j_bin[j2]=="1" and map[i2][j2]=="#":
                    count-=1
        if tot - count==K:
            ans+=1
            #print(i_bin,j_bin,count,tot-count)
print(ans)
