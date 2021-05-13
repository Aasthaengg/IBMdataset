n, m = map(int, input().split())
x = [list(map(int, input().split())) for x in range(n)]

# print(x)
x.sort()
sum = 0
yen = 0
for i in range(n):
    sum += x[i][1]
    yen += x[i][0] * x[i][1]
    if sum >= m:
        yen -= (sum-m)*x[i][0]
        break

print(yen)
