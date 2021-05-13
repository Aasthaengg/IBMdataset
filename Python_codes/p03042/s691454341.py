s=input()
s1=s[0]+s[1]
s2=s[2]+s[3]
n1=int(s1)
n2=int(s2)
if 1<=n1<=12:
    if 1<=n2<=12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 1<=n2<=12:
        print('YYMM')
    else:
        print('NA')