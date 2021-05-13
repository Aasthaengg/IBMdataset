n = int(input())
s = [input() for _ in range(2)]

ans = 1
law = 10 ** 9 + 7

i = 0
while i < n:
    if s[0][i] == s[1][i]:
        if i == 0:
            ans *= 3
        else:
            ans *= 3 - len({s[0][i-1], s[1][i-1]})
        i += 1
    else:
        if i == 0:
            ans *= 6
        else:
            if s[0][i-1] == s[1][i-1]:
                ans *= 2
            else:
                ans *= 3
        i += 2
    ans %= law
print(ans)