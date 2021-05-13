def f(S):
    L=list(S)
    L.sort()
    return  "".join(L)

N=int(input())
D={}

for _ in range(N):
    T=f(input())
    if T in D:
        D[T]+=1
    else:
        D[T]=1

A=0
for k in D:
    A+=(D[k]*(D[k]-1))//2
print(A)
