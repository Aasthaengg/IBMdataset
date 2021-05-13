N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
con = 0

for i in range(N-1):
    con += A[i+1] - A[i]

print(con)