s = input()
mae = int(s[:2])
ato = int(s[2:])

flag1 = 0
flag2 = 0
if 0<mae and mae<=12:
    flag1 = 1
if 0<ato and ato<=12:
    flag2 = 1

if flag1 == 1 and flag2 == 1:
    print('AMBIGUOUS')
elif flag1 == 1:
    print('MMYY')
elif flag2 == 1:
    print('YYMM')
else:
    print('NA')