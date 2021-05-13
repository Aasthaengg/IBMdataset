
N = int(input())
A = []
for _ in range(2):
    temp = list(map(int, input().strip().split()))
    A.append(temp)

total = 0

for j in range(N):
    row = 0
    col = 0
    total_temp = 0
    while col < N:
        if col == j:
            total_temp += A[row][col]
            row += 1
        total_temp += A[row][col]
        col += 1
    if total < total_temp:
        total = total_temp

print(total)
