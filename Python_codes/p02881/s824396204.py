n = int(input())
ans = 10 ** 12
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        distance = (n // i - 1) + (i - 1)
        ans = min(ans, distance)
    else:
        pass
print(ans)