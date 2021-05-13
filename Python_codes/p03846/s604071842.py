def get_pow(x, n):
    if n == 0:
        return 1
    ans = get_pow(x * x % 1000000007, int(n / 2))
    if n % 2 == 1:
        ans *= x
        ans %= 1000000007
    return ans

n = int(input())
a = list(map(int, input().split()))
c = [2] * ((n + 1) // 2)
if n % 2 == 1:
    c[0] = 1
for i in a:
    c[i // 2] -= 1
if c == [0] * len(c):
    print(get_pow(2, n // 2))
else:
    print(0)