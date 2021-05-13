N,M=map(int,input().split())
H=list(map(int,input().split()))
MaxH=[0]*N
z=0
for i in range(M):
    a,b=map(int,input().split())
    MaxH[a-1]=max(MaxH[a-1],H[b-1])
    MaxH[b-1]=max(H[a-1],MaxH[b-1])

for i in range(N):
    if H[i]>MaxH[i]:
        z+=1
print(z)