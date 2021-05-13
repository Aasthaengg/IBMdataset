A,B,M=map(int,input().split())

X=[10**10]+list(map(int,input().split()))
Y=[10**10]+list(map(int,input().split()))

K=min(X)+min(Y)

for _ in range(M):
    x,y,c=map(int,input().split())
    K=min(K,X[x]+Y[y]-c)
print(K)
