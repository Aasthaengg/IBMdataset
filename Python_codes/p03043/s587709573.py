import math

N,K=map(int,input().split())
p=math.ceil(math.log(K,2))
#print(p)
x=N*(2**p)
#print(x)
s=0

for n in range(1,N+1):
    if n>=K:
        s+=(x//N)
    else:
        q=math.ceil(math.log(K/n,2))
        s+=2**(p-q)
        #print(n,2**(p-q))

print(s/x)