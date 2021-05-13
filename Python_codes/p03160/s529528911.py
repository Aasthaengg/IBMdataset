N=int(input())
*H,=map(int,input().split())

D=[10**4*N]*N

D[0]=0
for i in range(N):
    if 1<=i:
        #print(i,H[i],H[i-1],abs(H[i]-H[i-1]))
        D[i]=min(D[i],abs(H[i]-H[i-1])+D[i-1])
    if 2<=i:
        #print(i,H[i],H[i-2],abs(H[i]-H[i-2]))
        D[i]=min(D[i],abs(H[i]-H[i-2])+D[i-2])
print(D[-1])