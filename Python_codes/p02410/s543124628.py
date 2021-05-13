n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
for i in range(m):
    b = int(input())
    for j in range(n):
        A[j][i] *= b
for j in range(n):
    print(sum(A[j]))
