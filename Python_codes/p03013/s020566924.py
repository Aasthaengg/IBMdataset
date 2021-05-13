N,M=map(int, input().split())
A=[int(input()) for _ in range(M)]

A=set(A)
D=[0]*(N+1)
D[0]=1

direction=[1,2]

for i in range(1,N+1):
 if i in A: continue
 # print([abs(H[i]-H[i-a])+D[i-a] for a in [1,2]])
 cnt=0
 for d in direction:
    prv=i-d
    if 0<=prv and not(prv in A): 
        cnt=cnt+D[prv]
        #print(i, prv,D[prv])

 D[i]=cnt
print(D[-1] % 1000000007)