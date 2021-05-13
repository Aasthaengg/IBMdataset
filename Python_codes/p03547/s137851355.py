x,y=input().split()
e=list("ABCDEF")
if x==y:
    print('=')
elif e.index(x)>e.index(y):
    print('>')
else:
    print('<')