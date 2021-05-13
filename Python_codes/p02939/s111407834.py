s = input()

if len(s) == 1:
    print(1)
    exit()


now = s[0]
cnt = 1
i = 1
while True:
    if s[i] != now:
        cnt += 1
        now = s[i]
        i += 1
    else:
        now = now + s[i]
        cnt += 1
        i += 2
        if i > len(s):
            cnt -= 1
    if i >= len(s):
        break
print(cnt)