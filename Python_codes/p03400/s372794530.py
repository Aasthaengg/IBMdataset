N = int(input())
D, X = map(int,input().split())
A = [int(input()) for _ in range(N)]

C = [0]*D
for a in A:
    n = 0
    while a*n < D:
        C[a*n] += 1
        n += 1
print(sum(C)+X)