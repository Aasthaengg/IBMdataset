a,b,c,d=map(int,input().split())
d_ca=max(a,c)-min(a,c)
d_ab=max(a,b)-min(a,b)
d_bc=max(b,c)-min(b,c)
if d_ca<=d:
    print('Yes')
elif d_bc<=d and d_ab<=d:
    print('Yes')
else:
    print('No')