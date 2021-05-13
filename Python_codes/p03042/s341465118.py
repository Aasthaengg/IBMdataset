s = input()
sb = s[:2]
sa = s[2:]
if 1<=int(sb)<=12 and (13 <= int(sa) or int(sa)==0):
    print('MMYY')
elif 1<=int(sa)<=12 and (13 <= int(sb) or int(sb)==0):
    print('YYMM')
elif 1<=int(sb)<=12 and 1<=int(sb)<=12:
    print('AMBIGUOUS')
else:
    print('NA')
