s = input()
t = input()
ans = len(t)

for i in range(len(s)):
    if i+len(t) > len(s):
        break
    u = s[i:i+len(t)]
    cnt = 0
    for j in range(len(t)):
        if t[j] != u[j]:
            cnt += 1
    ans = min(ans, cnt)
print(ans)