x,y=map(str,input().split())
arr=['A','B','C','D','E','F']
if arr.index(x)<arr.index(y):
    print('<')
elif arr.index(x)>arr.index(y):
    print('>')
else:
    print('=')