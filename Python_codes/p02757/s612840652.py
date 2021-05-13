n, p = map(int, input().split())
s = list(input())
s.reverse()
ans = 0

if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += n - i
else:
    modlist = [0] * (n + 1)
    ten = 1
    for i in range(n):
        mod_now = (int(s[i]) * ten) % p
        modlist[i + 1] = (modlist[i] + mod_now) % p
        ten *= 10
        ten %= p
    countlist = [0] * p
    for i in range(n + 1):
        ans += countlist[modlist[i]]
        countlist[modlist[i]] += 1
print(ans)