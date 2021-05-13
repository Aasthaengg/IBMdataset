N=int(input())
P=["*"]+list(map(int,input().split()))

X=0
S=0
for i in range(1,N+1):
    if P[i]==i:
        S+=1
    else:
        X+=(S+1)//2
        S=0
X+=(S+1)//2
print(X)
