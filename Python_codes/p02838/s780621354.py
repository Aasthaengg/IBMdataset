n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7
bits = [0]*60
for x in a:
    i = 0
    while x > 0:
        if x % 2 == 1:
            bits[i] += 1
        x //= 2
        i += 1
ans = 0
for i in range(60):
    ans += (bits[i] * (n-bits[i])) * pow(2, i, mod)
    ans %= mod
print(ans)