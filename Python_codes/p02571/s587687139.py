s = input()
t = input()

ans = len(t)

for i in range(len(s) - len(t) + 1):
    sub = s[i:i+len(t)]
    cnt = 0
    for j in range(len(t)):
        if sub[j] != t[j]:
            cnt = cnt + 1
    ans = min(ans, cnt)

print(ans)