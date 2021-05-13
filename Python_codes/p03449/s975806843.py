N = int(input())
A = [[int(i) for i in input().split()] for j in range(2)]
count = 0
Max = 0

for i in range(N):
    for j in range(i+1):
        count += A[0][j]
    for j in range(N-i):
        count += A[1][i+j]
    Max = max(Max, count)
    count = 0

print(Max)
