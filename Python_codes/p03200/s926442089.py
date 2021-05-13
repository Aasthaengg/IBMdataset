s = list(str(input()))
bCnt = 0
ans = 0

for i in s:
    if i == 'B':
        bCnt += 1
    else:
        ans += bCnt

print(ans)