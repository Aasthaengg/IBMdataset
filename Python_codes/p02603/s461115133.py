n = int(input())
A = [0] + [*map(int, input().split())] + [0]
dp_yen = [0]*(n+1)
dp_yen[1] = 1000
for day in range(1, n):
    stock = 0
    if A[day] > 0: stock = dp_yen[day] // A[day]
    remain = dp_yen[day] - stock*A[day]
    dp_yen[day+1] = max(dp_yen[day], remain + stock * A[day+1])
print(dp_yen[n])
