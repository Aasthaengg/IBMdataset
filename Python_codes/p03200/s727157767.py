s = list(input())

ans = 0

cntB = 0

for i in range(len(s)):
    if s[i] == 'B':
        cntB += 1
    else:
        ans += cntB

print(ans)