s = input()
n = len(s)-1
ans = 0
for i in range(2**n):
    now = s[0]
    for j in range(n):
        if (i>>j) & 1 == 1:
            ans += int(now)
            now = s[j+1]
        else:
            now += s[j+1]
    ans += int(now)
print(ans)