from collections import *
from itertools import *
import copy
from heapq import *


N,M,R=map(int,input().split())
Rlst=list(map(int,input().split()))
ABC=[list(map(int,input().split())) for i in range(M)]

data=[[] for i in range(N+1)]
nagasa={}
for a,b,c in ABC:
    data[a].append(b)
    data[b].append(a)
    A,B=min(a,b),max(a,b)
    nagasa.update({str(A)+" "+str(B):c})
mokutekiti=[[100000*200+1 for i in range(R)] for m in range(R)]
for r1i in range(R-1):
    for r2i in range(r1i+1,R):
        r1=Rlst[r1i]
        r2=Rlst[r2i]
        visited=set()
        stack=[0]
        heapify(stack)
        dic={0:[r1]}
        while stack:
            m=heappop(stack)
            #if not m in visited:
            #visited.add(m)
            a=dic[m].pop()
            if not a in visited:
                visited.add(a)
                for b in data[a]:
                    if not b in visited or b==r2:
                        A,B=min(a,b),max(a,b)
                        tempm=m+nagasa[str(A)+" "+str(B)]
                        if b==r2:
                            if mokutekiti[r1i][r2i]>tempm:
                                mokutekiti[r1i][r2i]=tempm
                                mokutekiti[r2i][r1i]=tempm
                        else:
                            heappush(stack,tempm)
                            if tempm in dic:
                                dic[tempm].append(b)
                            else:
                                dic.update({tempm:[b]})



value=[]
for lst in permutations([i for i in range(R)],R):
    nagasa=0
    for i in range(R-1):
        nagasa+=mokutekiti[lst[i]][lst[i+1]]
    value.append(nagasa)
print(min(value))
