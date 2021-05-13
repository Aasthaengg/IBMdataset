X,Y=map(str, input().split())
str_list = 'ABCDEF'
x=str_list.index(X)
y=str_list.index(Y)
if x<y : print('<')
if x==y: print('=')
if x>y : print('>')
