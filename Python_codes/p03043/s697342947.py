from math import *
N,K=list(map(int,input().split()))
out=0
for n in range(1,N+1):
    if n>=K:
        out+=1/N
    else:
        out+=(1/N)*(1/2)**(ceil(log(K/n,2)))
print(out)