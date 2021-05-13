n = int(input())
x = [0] + list(map(int, input().split()))
y = [0] + list(map(int, input().split()))
tmp = [[0 for i in range(3)] for j in range(n+1)]
max = 0
for i in range(1, n+1, 1):
    absDiff = abs(x[i]-y[i])
    tmp[i][0] += tmp[i-1][0] + absDiff
    tmp[i][1] += tmp[i-1][1] + absDiff ** 2
    tmp[i][2] += tmp[i-1][2] + absDiff ** 3
    if absDiff > max:
        max = absDiff
print(tmp[n][0])
print(tmp[n][1] ** (1/2))
print(tmp[n][2] ** (1/3))
print(max)