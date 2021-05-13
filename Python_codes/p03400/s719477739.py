N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]
for i in range(N):
    for j in range(1, D+1):
        if ( j - 1 ) % A[i] == 0:
            X += 1
print(X)
