N=int(input())
A=list(map(int,input().split()))

T={}
for a in A:
    if a in T:
        T[a]+=1
    else:
        T[a]=1

K=0
for b in T:
    if T[b]<b:
        K+=T[b]
    elif b<T[b]:
        K+=T[b]-b
print(K)
