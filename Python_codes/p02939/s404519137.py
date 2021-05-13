s = input()
ans = 0
n = len(s)
prev = ""
now = 0
while now<n:
    if prev != s[now]:
        prev = s[now]
        now += 1
    else:
        if now != n-1:
            now += 2
            prev = ""
        else:
            break
    ans += 1
print(ans)