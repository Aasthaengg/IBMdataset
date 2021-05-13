N = int(input())
ans = 0

if len(str(N)) % 2 != 0:
    sub = 10 ** (len(str(N))) - N - 1

    for i in range(len(str(N)), 0, -2):
        ans += 10 ** i - 10 ** (i-1)
    ans -= sub
    print(ans)
else:
    digits = len(str(N)) - 1
    for i in range(digits, 0, -2):
        ans += 10 ** i - 10 ** (i-1)
    print(ans)
