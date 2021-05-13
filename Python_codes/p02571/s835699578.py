s = input()
t = input()

ans = 1001001001
for i in range(len(s)-len(t)+1):
    _s = s[i:i+len(t)]
    cnt = 0
    for j in range(len(t)):
        if t[j] != _s[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)