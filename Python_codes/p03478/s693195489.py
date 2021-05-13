n, a, b = list(map(int, input().split()))
ans = 0


def dsum(n):
    wa = 0
    while n > 0:
        wa += n % 10
        n //= 10
    return wa


for i in range(1, n + 1):
    res = i
    if a <= dsum(i) <= b:
        ans += i

print(ans)
