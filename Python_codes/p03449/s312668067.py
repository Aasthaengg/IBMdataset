N = int(input())
x = [list(map(int, input().split())) for i in range(2)]
sum = 0
max = 0
for i in range(N):
    for k in range(i, N):
        sum += x[1][k]
    for j in range(i+1):
        sum += x[0][j]
    if max < sum:
        max = sum
    sum = 0
print(max)