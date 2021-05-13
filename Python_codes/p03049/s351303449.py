n = int(input())
s = [str(input()) for _ in range(n)]

ba = 0
bo = 0
oa = 0
ans = 0

for i in range(n):
    ans += s[i].count('AB')
    if s[i][0] == 'B' and s[i][-1] == 'A':
        ba += 1
    elif s[i][0] == 'B':
        bo += 1
    elif s[i][-1] == 'A':
        oa += 1
#print(ans, ba, min(bo, oa))

if ba > 0 and bo + oa > 0:
    ans += ba + min(bo, oa)
if ba > 0 and bo + oa == 0:
    ans += ba - 1
if ba == 0 and bo + oa > 0:
    ans += min(bo, oa)

print(ans)