import numpy as np
N,M,X=map(int,input().split())
allList=[]
for _ in range(N):
    allList.append(np.array(list(map(int,input().split()))))
minnum=10**7
for i in range(2**N):
    skill=[0]*(M+1)
    flag=True
    for row in range(N):
        if i&(2**row)>0:
            skill+=allList[row]
    for j in range(M):
        if skill[j+1]<X:
            flag=False
    if flag:
        minnum=min(minnum,skill[0])
if minnum==10**7:
    minnum=-1
print(minnum)