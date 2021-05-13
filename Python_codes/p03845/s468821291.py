N=int(input())
T=list(map(int,input().split()))
M=int(input())
S=sum(T)

for i in range(M):
    a,b=map(int,input().split())
    SS=S-T[a-1]+b
    print(SS)