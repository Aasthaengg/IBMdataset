import re
s = input()
f = s[:2]
b = s[2:]
flg_fm = False
flg_bm = False

if f[0] == '0' and bool(re.search('[1-9]', f[1])) or f[0] == '1' and bool(re.search('[0-2]', f[1])):
    flg_fm = True
if b[0] == '0' and bool(re.search('[1-9]', b[1])) or b[0] == '1' and bool(re.search('[0-2]', b[1])):
    flg_bm = True

if flg_fm and flg_bm:
    print('AMBIGUOUS')
elif flg_bm:
    print('YYMM')
elif flg_fm:
    print('MMYY')
else:
    print('NA')