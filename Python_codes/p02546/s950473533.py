x= str(input())
a=list(x)
l=len(a)
if a[l-1]=='s':
    print(x+'es')
else:
    print(x+'s')