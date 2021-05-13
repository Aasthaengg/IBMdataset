a, b, c, x  = [int(input()) for _ in range(4)]
x //= 50
ans = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            p = 10 * i + 2 * j + k
            if p == x:
                ans += 1
print(ans)