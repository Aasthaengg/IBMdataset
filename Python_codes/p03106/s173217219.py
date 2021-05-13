import math
A,B,K=map(int,input().split())
anslist=[]
for i in range(1,max(A,B)+1):
    if (A%i==0)&(B%i==0):
        anslist.append(i)
print(anslist[0-K])