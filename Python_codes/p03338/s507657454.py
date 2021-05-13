n = int(input())
s = input()

ans = 0
for i in range(n):
    d1, d2 = {}, {}
    for j in range(i):
        d1[s[j]] = 0
    for j in range(i, n):
        if s[j] in d1 and s[j] not in d2:
            d2[s[j]] = 0
    ans = max(ans, len(d2))

print(ans)


