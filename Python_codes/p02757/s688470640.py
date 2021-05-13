n, p = map(int, input().split())
s = input()

ans = 0
if p == 2:
    for i, char in enumerate(s):
        if int(char) % 2 == 0:
            ans += i + 1
    print(ans)

elif p == 5:
    for i, char in enumerate(s):
        if int(char) % 5 == 0:
            ans += i + 1
    print(ans)

else:
    a = [0] * (n + 1)
    for i in range(n):
        a[i + 1] = a[i] + int(s[n - i - 1]) * pow(10, i, p)
        a[i + 1] %= p
    memo = {}
    for i in range(n + 1):
        if a[i] not in memo:
            memo[a[i]] = 1
        else:
            memo[a[i]] += 1
    for i in memo:
        ans += memo[i]* (memo[i] - 1) // 2
    print(ans)