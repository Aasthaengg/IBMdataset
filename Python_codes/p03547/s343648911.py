x,y = input().split()
li = ['A','B','C','D','E','F']
x = li.index(x)
y = li.index(y)
if x < y:
    print('<')
elif x > y:
    print('>')
else:
    print('=')