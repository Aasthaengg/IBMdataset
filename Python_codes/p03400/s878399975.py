N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(N):
    X += len([d for d in range(D) if d*A[i]+1 <= D])
print(X)