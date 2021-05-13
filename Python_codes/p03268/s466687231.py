n, k = map(int, input().split())

ans = (n // k) ** 3

if k % 2 == 0:
    tmpN = n - k / 2
    ans += (tmpN // k + 1) ** 3


print(int(ans))