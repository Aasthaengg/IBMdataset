a, b, x = map(int, input().split())

if a%x != 0:
    aa = a + (x - a % x)
else: aa = a

ans = (b - aa) // x + 1

print(ans)