N,K=map(int,input().split())
T={}
for _ in range(N):
    a,b=map(int,input().split())
    if a in T:
        T[a]+=b
    else:
        T[a]=b
U=sorted(T)

for a in U:
    if T[a]>=K:
        print(a)
        break
    else:
        K-=T[a]
