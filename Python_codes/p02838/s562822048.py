N = int(input())
A = tuple(map(int, input().split()))
MOD = 10 ** 9 + 7

ans = 0
x = 1
for d in range(60):
    odd = 0
    even = 0
    for a in A:
        if a & (1 << d):
            odd += 1
        else:
            even += 1
    ans += odd * even * x
    ans %= MOD
    x <<= 1
print(ans)