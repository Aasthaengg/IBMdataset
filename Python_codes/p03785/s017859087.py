N,C,K=map(int,input().split())
T=sorted([int(input()) for i in range(N)])
cnt=0
i=0
while(i<N):
    j=i
    lim=T[i]+K
    while(j<N and T[j]<=lim and j-i+1<=C):
        j+=1
    cnt+=1
    i=j
print(cnt)