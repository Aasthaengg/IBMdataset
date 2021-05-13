S = int(input())
b=S%100
a=S//100
if 1<=a<=12 and 1<=b<=12:
    print('AMBIGUOUS')

elif 1<=a<=12:
    print('MMYY')

elif 1<=b<=12:
    print('YYMM')

else:
    print('NA')

