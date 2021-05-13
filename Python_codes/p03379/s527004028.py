N = int(input())
X = list(map(int,input().split()))
X.insert(0,0)
A = sorted(X[:])
a = A[N//2]
b = A[N//2+1]
for i in range(1,N+1):
    if X[i]>a:
        print(a)
    else:
        print(b)