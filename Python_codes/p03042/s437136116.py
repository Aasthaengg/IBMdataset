a=input()
n=int(a[0:2])
m=int(a[2:4])
if 0<n<=12 and 0<m<=12:
    print('AMBIGUOUS')
elif 0<n<=12:
    print('MMYY')
elif 0<m<=12:
    print('YYMM')
else:
    print('NA')