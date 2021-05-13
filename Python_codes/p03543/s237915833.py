s = input()
prev = s[0]
cnt = 1
ans = 0
for i in range(1, 4):
    if prev == s[i]:
        cnt += 1
    else:
        prev = s[i]
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
if ans >= 3:
    print('Yes')
else:
    print('No')