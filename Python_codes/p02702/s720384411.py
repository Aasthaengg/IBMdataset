S=list(map(int,input()))
L=len(S)
M=2019
d=10

U=[]
for x in range(L):
    if x==0:
        U=[1]
    else:
        U.append((U[-1]*d)%M)
        
T=[0]
for x in range(1,L+1):
    T.append((T[-1]+S[-x]*U[x-1])%M)

D={}
for x in T:
    if x in D:
        D[x]+=1
    else:
        D[x]=1

r=0
for x in D.values():
    r+=(x*(x-1))//2

print(r)
