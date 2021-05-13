a,b,c,d=map(int,input().split())
n=max(a,b)-min(a,b)
m=max(b,c)-min(b,c)
o=max(a,c)-min(a,c)
if o<=d:
    print('Yes')
elif n<=d and m<=d:
    print('Yes')
else:
    print('No')