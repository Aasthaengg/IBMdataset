from itertools import permutations 
n,m=map(int,input().split())
cost=[]
for i in range(m):
    cost.append([int(i) for i in input().split()])
clr=[]
for i in range(n):
    clr.append([int(i) for i in input().split()])
l=[i for i in range(m)]
ind=[[0 for j in range(m)] for i in range(4)]
for i in range(n):
    for j in range(n):
        curr=(i+1+j+1)%3 
        ind[curr][clr[i][j]-1]+=1 
mini=10**9 
for i in range(m):
    for j in range(m):
        for k in range(m):
            if i==j or i==k or j==k:
                continue 
            curr=0 
            for it in range(3): 
                for it1 in range(m): 
                    if it==0:
                        k1=i 
                    elif it==1:
                        k1=j 
                    else:
                        k1=k 
                    curr+=ind[it][it1]*cost[it1][k1] 
            mini=min(mini,curr)
print(mini)
