N=int(input())
L=list(map(int,input().split()))
L.sort()
K=0


for i in range(N-2):
    for j in range(N-i-1):
        for k in range(N-i-j-2):
            if L[i]<L[i+j+1]<L[i+j+k+2]and L[i]+L[i+j+1]>L[i+j+k+2]:
                K=K+1
print(K)