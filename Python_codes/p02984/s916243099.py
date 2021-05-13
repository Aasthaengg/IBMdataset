N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
X = [0 for _ in range(N+1)]
x = A[1]-A[2]
for i in range(3,N+1):
    if i%2==0:
        x -= A[i]
    else:
        x += A[i]
X[1] = x//2
for i in range(2,N+1):
    X[i] = A[i-1]-X[i-1]
for i in range(1,N+1):
    X[i] = 2*X[i]
print(*X[1:])