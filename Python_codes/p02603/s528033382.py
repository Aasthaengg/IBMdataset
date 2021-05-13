n = int(input())
A = [*map(int, input().split())] + [0]
dp_yen = [1000]*(n+1)
for day in range(n):
    dp_yen[day+1] = max(dp_yen[day], dp_yen[day] + dp_yen[day]//A[day] * (A[day+1] - A[day]))
print(dp_yen[n])
