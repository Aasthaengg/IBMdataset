a=input().split()
a=[int(a[i]) for i in (0,1,2)]
a=list(dict.fromkeys(a))
if len(a)==2:
    print('Yes')
else:
    print('No')