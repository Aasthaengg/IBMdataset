lst=['A','B','C','D','E','F']
a=input()
if lst.index(a[0])>lst.index(a[2]):
    print('>')
elif lst.index(a[0])==lst.index(a[2]):
    print('=')
else:
    print('<')