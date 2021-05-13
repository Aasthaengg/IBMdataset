N,K=map(int,input().split())
P=[1]
for k in range(17):
    P.append(P[-1]/2)

Q=0
for i in range(1,N+1):
    u=0
    x=i
    while x<K:
        u+=1
        x*=2
    Q+=P[u]

print(Q/N)
