I=input().split( )
n=int(I[0])
m=int(I[1])

C=input().split( )
c=[int(C[i]) for i in range(m)]

T=[50001 for i in range(n+1)]#50000が上限
T[0]=0

for i in range(m):
    for j in range(n+1):
        if c[i]+j<=n:
            T[j+c[i]]=min(T[j+c[i]],T[j]+1)

print(T[n])

