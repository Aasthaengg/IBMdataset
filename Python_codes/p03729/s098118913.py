s=input().split()
a=s[0]
b=s[1]
c=s[2]
if a[len(a)-1]==b[0] and b[len(b)-1]==c[0]:
    print('YES')
else:
    print('NO')
