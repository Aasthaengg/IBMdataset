n = int(input())
ans = 0
def calc(x):
    x -= 1
    if x <= 0:
        return 0
    elif n // x == n % x:
        return x
    return 0

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        ans += calc(n // i) + calc(i)
print(ans)