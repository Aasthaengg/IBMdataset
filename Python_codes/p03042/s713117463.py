s = input()
first = 0 < int(s[:2]) < 13
second = 0 < int(s[2:]) < 13

if first and second:
    print('AMBIGUOUS')
elif first:
    print('MMYY')
elif second:
    print('YYMM')
else:
    print('NA')
