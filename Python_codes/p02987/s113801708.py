S=input()
l=[]
n=[]
l.extend(S)
a=set(l)
if len(a)==2:
    print('Yes')
else:
    print('No')