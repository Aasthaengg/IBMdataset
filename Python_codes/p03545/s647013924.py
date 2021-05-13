a=list(map(int,list(input())))
s=[]
for i in range(2**3):
    calc=a[0]
    s=[str(a[0])]
    for j in range(3):
        if i>>j&1:
            calc+=a[j+1]
            s.append('+')
        else:
            calc-=a[j+1]
            s.append('-')
        s.append(str(a[j+1]))
    if calc==7:
        break
print(''.join(s)+'=7')