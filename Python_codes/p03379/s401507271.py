N = int(input())
X = list(map(int,input().split()))

sor = sorted(X)
l = sor[N//2-1]
r = sor[N//2]
for i in range(0,N,1):
    print(l if X[i]>=r else r)