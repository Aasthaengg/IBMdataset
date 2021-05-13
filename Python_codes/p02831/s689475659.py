a, b = map(int, input().split())
ans = 10**100
for i in range(min(a, b), 1, -1):
    if a % i == 0 and b % i == 0:
        ans = i * (a // i) * (b // i)
        break
print(min(a * b, ans))