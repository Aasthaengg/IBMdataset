x,y=map(str,input().split())
a=['A','B','C','D','E','F']
x=a.index(x)
y=a.index(y)
if x>y:
    print('>')
elif x<y:
    print('<')
else:
    print('=')