n = int(input())
s1 = input()
s2 = input()

ans = 1
prev = 0
i = 0
while i < len(s1):
    if s1[i] == s2[i]:
        ans *= (3 - prev)
        prev = 1
        i += 1
    else:
        if prev == 0:
            ans *= 6
        elif prev == 1:
            ans *= 2
        else:
            ans *= 3
        prev = 2
        i += 2
    ans %= 1000000007
print(ans)
