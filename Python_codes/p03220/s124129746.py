N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
nin=10**6
ans=0

for i in range(N):
    ave=T-H[i]*0.006
    dif=abs(A-ave)
    if dif<nin:
        ans=i
        nin=dif

print(ans+1)