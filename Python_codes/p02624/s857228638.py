x = int(input())

ans = 0
for i in range(1, x+1):
    k = x // i
    ans += i * k * (k+1) // 2

print(ans)
