import sys

N,K=map(int,input().split())
S=list(map(int,input()))

T=[]
t=1
k=0
for i in range(N):
    if t==S[i]:
        k+=1
    else:
        t^=1
        T.append(k)
        k=1
T.append(k)
if S[-1]==0:
    T.append(0)

X=len(T)
if K>=X//2:
    print(N)
    sys.exit()

M=sum(T[:2*K+1])
F=M
for i in range(X//2-K):
    F=F-(T[2*i]+T[2*i+1])+(T[2*(i+K)+1]+T[2*(i+K+1)])
    M=max(M,F)

print(M)
