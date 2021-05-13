N = int(input())
A = list(map(int,input().split()))
X = sorted(A,reverse=False)

for i in range(N):
    if A[i] < X[N//2 ]:
        print(X[N//2 ])
    else:
        print(X[N//2 - 1])
