S = input()
lenS = len(S)
bcnt = S.count('B')
wcnt = lenS - bcnt
if bcnt > wcnt:
    ms = 'W'
    rc = wcnt
else:
    ms = 'B'
    rc = bcnt
sum = 0

for i, s in enumerate(S):
    if rc == 0:
        break
    if s == ms:
        if ms == 'W':
            sum += i-rc+1
        elif ms == 'B':
            sum += lenS-i-rc
        rc -= 1
print(sum)