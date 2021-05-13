def pow_mod(n, k, m):
    if k == 0:
        return 1
    if k & 1:
        return (pow_mod(n, k - 1, m) * n % m) % m
    else:
        return (pow_mod(n, k // 2, m) ** 2) % m

n = int(input())
aaa = list(map(int, input().split()))
mod = 10 ** 9 + 7
aaa.sort()
if n % 2 == 0:
    for i in range(0, n, 2):
        if aaa[i] != aaa[i + 1]:
            print(0)
            exit()
    print(pow_mod(2, (n // 2), mod))
else:
    for i in range(1, n, 2):
        if aaa[i] != aaa[i + 1]:
            print(0)
            exit()
    print(pow_mod(2, ((n - 1) // 2), mod))