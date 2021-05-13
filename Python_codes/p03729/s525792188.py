a,b,c=input().split()
ra=a[::-1]
rb=b[::-1]
if ra[0]==b[0] and rb[0]==c[0]:
    print('YES')
else:
    print('NO')