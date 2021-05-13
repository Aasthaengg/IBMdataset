
x,y=map(str,input().split())

l=list('ABCDEF')

xi=l.index(x)
yi=l.index(y)

if (xi<yi):print('<')
elif (xi>yi):print('>')
else:print('=')