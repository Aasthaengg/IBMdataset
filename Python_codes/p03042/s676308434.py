s = input()
s1, s2 = s[:2],s[2:]
if s1>'12' and s2>'12':
    print('NA')
elif s1<='12' and s2<='12':
    if s1 == '00' and s2!='00':
        print('YYMM')
    elif s2 == '00' and s1!='00':
        print('MMYY')
    elif s1 =='00' and s2 =='00':
        print('NA')
    else :
        print('AMBIGUOUS')
elif s1<='12' and s2>'12':
    print('NA' if s1 == '00' else 'MMYY')   
elif s2<='12' and s1>'12':
    print('NA' if s2 == '00' else 'YYMM')
else:
    print('NA')