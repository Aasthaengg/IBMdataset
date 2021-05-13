from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=int(1e9)+7

###############################################################################\n=17
X=[False]*(10**6+1)
P=[]
for i in range(2,len(X)):
    if X[i] is False:
        for j in range(2*i,len(X),i):
            X[j]=True
for i in range(2,len(X)):
    if X[i] is False:
        P.append(i)


n=int(input())
A=INPUT()
ans=0
V=[0]*(10**6+1)
for i in range(n):
    ans=math.gcd(ans,A[i])
    V[A[i]]+=1
if ans==1:
    bool=True
    for i in range(2,10**6+1):
        if V[i]>=2:
            bool=False
            break
    if bool:
        for ele in P:
            c=0
            for i in range(ele,10**6+1,ele):
                if V[i]>0 and i%ele==0:
                    c+=1
            if c>1:
                bool=False
                break
        if bool:
            print("pairwise coprime")
        else:
            print("setwise coprime")
    else:
        print("setwise coprime")
else:
    print("not coprime")
