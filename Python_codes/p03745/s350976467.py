N = int(input())
ans = 1
A = list(map(int, input().split()))
prev = A[0]
trend = 0
for a in A[1:]:
    if (a - prev) * trend < 0:
        ans += 1
        trend = 0
    elif trend == 0:
        if a - prev > 0:
            trend = 1
        elif a - prev < 0:
            trend = -1
    prev = a
print(ans)
