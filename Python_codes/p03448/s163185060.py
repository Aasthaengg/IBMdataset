a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0

for l in range(a + 1):
    for m in range(b + 1):
        for n in range(c + 1):
            s = 500 * l + 100 * m + 50 * n
            if s == x:
                ans += 1

print(ans)
