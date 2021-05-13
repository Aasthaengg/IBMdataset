n = int(input())
mod = 1000000007

a, b, c = (1, 1, 1)
for i in range(n):
    a = a * 10 % mod
    b = b * 9 % mod
    c = c * 8 % mod

ans = (a + c - 2 * b) % mod
print(ans)
