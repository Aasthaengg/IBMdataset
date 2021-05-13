N = int(input())
X = list(map(int,input().split()))
Y = sorted(X)
M2 = Y[N//2]
M1 = Y[N//2-1]
for i in range(N):
    if X[i]<=M1:
        print(M2)
    else:
        print(M1)
