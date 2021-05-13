s = list(input())

a = int(s[0]+s[1])
b = int(s[2]+s[3])

if  1<=a<=12 and 1<=b<=12:
  print('AMBIGUOUS')
elif (a>12 or a==0) and 1<=b<=12:
  print('YYMM')
elif (b>12 or b==0) and 1<=a<=12:
  print('MMYY')
elif (a>12 or a==0) and (b>12 or b==0):
  print('NA')