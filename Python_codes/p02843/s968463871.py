x = int(input())
kosuu, amari = x // 100, x % 100
ans = 0

for i in range(kosuu):
    amari -= 5
    if amari <= 0:
        ans = 1
        break

print(ans)
