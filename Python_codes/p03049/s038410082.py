n = int(input())
s = [input() for _ in range(n)]

cnt = 0
cnta = 0
cntb = 0
cntab = 0
for i in range(n):
    if 'AB' in s[i]:
        cnt += s[i].count('AB')
    if s[i][0] == 'B' and s[i][-1] == 'A':
        cntab += 1
    elif s[i][0] == 'B':
        cntb += 1
    elif s[i][-1] == 'A':
        cnta += 1
    
if cntab == 0:
    cnt += min(cnta, cntb)
else:
    if cnta + cntb > 0:
        cnt += cntab + min(cnta, cntb)
    else:
        cnt += cntab - 1
print(cnt)