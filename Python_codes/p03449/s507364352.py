N = int(input())
A = []
for _ in range(2):
    A.append(list(map(int, input().split())))

sum_candy = []

for i in range(N):
    sum = 0
    for j in range(i+1):
        sum += A[0][j]
    for j in range(i, N):
        sum += A[1][j]

    sum_candy.append(sum)

print(max(sum_candy))