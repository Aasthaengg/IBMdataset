s = input()
first = int(s[:2])
second = int(s[2:])

month = [False,False]


if(1 <= first and first <= 12):
    month[0] = True

if(1 <= second and second <= 12):
    month[1] = True
    
if(month[0] & month[1]):
    print('AMBIGUOUS')
elif(month[0]):
    print('MMYY')
elif(month[1]):
    print('YYMM')
else:
    print('NA')

