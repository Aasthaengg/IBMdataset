s = input().strip()
t = input().strip()

i = 0
ans = 0
while i + len(t) <= len(s):
    tmp = 0
    for j in range(len(t)):
        if t[j] == s[i + j]:
            tmp += 1
    ans = max(ans, tmp)
    i += 1
print(len(t) - ans)
