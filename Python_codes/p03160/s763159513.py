N=int(input())
*H,=map(int,input().split())
D=[-1]*N
D[0]=0
D[1]=abs(H[1]-H[0])
for i in range(2,N):
    D[i]=min(abs(H[i]-H[i-1])+D[i-1],abs(H[i]-H[i-2])+D[i-2])
print(D[-1])