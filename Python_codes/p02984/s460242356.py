N = int(input())
A = list(map(int,input().split()))
a = A[0]
for i in range(1,N):
    if i%2==0:
        a += A[i]
    else:
        a -= A[i]
X = [0 for _ in range(N)]
X[0] = a//2
for i in range(1,N):
    X[i] = A[i-1]-X[i-1]
X = [2*X[i] for i in range(N)]
print(*X)