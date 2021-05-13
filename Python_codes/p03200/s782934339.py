s = input()
n = len(s)

ans, cntB = 0, 0
for i in range(n):
    if s[i] == 'B':
        cntB += 1
    else:
        ans += cntB

print(ans)