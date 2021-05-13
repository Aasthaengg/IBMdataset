S = input()
check = now = ''
ans = 0
for s in S:
    now += s
    if check != now:
        ans += 1
        now, check = '', now
print(ans)