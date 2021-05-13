s = input()

f = (0 < int(s[:2]) < 13)
s = (0 < int(s[2:]) < 13)
ans = 'NA'
if f and s:
    ans = 'AMBIGUOUS'
elif s:
    ans = 'YYMM'
elif f:
    ans = 'MMYY'
print(ans)
