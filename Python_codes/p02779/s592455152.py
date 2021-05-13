n=int(input(''))
a=list(map(int,input('').split(' ')))
b={}
for i in range(n):
    if str(a[i]) in b:
        b[str(a[i])]+=1
    else:
        b[str(a[i])]=1

ok=1
for i in b:
    if b[i]>=2:
        ok=0
        break

if ok==0:
    print('NO')
else:
    print('YES')