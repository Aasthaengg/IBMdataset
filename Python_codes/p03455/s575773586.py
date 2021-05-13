a,b=(int(x) for x in input().split())
c = int(a)*int(b)
e = c % 2
if e ==  0:
    print('Even')
else:
    print('Odd')