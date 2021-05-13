N = int(input())


def f(x):
    result = N // x
    return result

ans = 0
for x in range(1, N + 1):
    Y = f(x)
    ans += x * Y * (Y + 1) / 2
print(int(ans))