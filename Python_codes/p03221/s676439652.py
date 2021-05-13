N,M=map(int,input().split())
l=[]
for i in range(M):P,Y=map(int,input().split());l.append([i,P,Y,0])
from operator import*
l.sort(key=itemgetter(2))
P=[0]*N
for i in range(M):P[l[i][1]-1]+=1;l[i][3]=P[l[i][1]-1]
l.sort(key=itemgetter(0))
for i in range(M):print(str(l[i][1]).zfill(6)+str(l[i][3]).zfill(6))
