N,M=map(int,input().split())

X=[0]*(M+1)
for _ in range(N):
    A=list(map(int,input().split()))[1:]
    for a in A:
        X[a]+=1
print(X.count(N))
