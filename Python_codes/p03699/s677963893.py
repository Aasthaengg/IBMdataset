N=int(input())

inf=float("inf")
X=[[-inf]*10 for _ in range(N+1)]

X[0][0]=0
for k in range(N):
    s=int(input())

    for a in range(10):
        X[k+1][a]=max(X[k][a],X[k][(a-s)%10]+s)

X[-1][0]=0
print(max(X[-1]))
