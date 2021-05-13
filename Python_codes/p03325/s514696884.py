n = int(input())
alst = list(map(int, input().split()))
ans = 0
for num in alst:
    while num % 2 == 0:
        num //= 2
        ans += 1
print(ans)