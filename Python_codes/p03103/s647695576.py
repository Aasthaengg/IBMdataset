n, m = map(int, input().split())
drink = [list(map(int, input().split())) for i in range(n)]
drink.sort()
ans = 0

for i, j in drink:
    if m != 0:
        if m >= j:
            ans += i * j
            m -= j
        else:
            ans += i * m
            break

print(ans)