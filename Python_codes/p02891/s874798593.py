s = list(input())
n = len(s)
k = int(input())
ans = 0
if s.count(s[0]) == n:
    ans = (n * k) // 2
else:
    c = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            c += 1
        else:
            ans += c // 2
            c = 1
    ans += c // 2
    ans *= k
    if s[0] == s[n - 1]:
        c1 = 0
        c2 = 0
        for i in range(n):
            if s[i] == s[0]:
                c1 += 1
            else:
                break
        for i in range(n - 1, -1, -1):
            if s[i] == s[n - 1]:
                c2 += 1
            else:
                break
        if not c1 // 2 + c2 // 2 == (c1 + c2) // 2:
            ans += k
            ans -= 1
print(ans)