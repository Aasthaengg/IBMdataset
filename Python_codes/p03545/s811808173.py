a=[int(c) for c in input()]

for i in range(2**3):
    s=a[0]
    ss=str(a[0])
    for j in range(3):
        if (i>>j)&1==1:
            s+=a[j+1]
            ss=ss+'+'+str(a[j+1])
        else:
            s-=a[j+1]
            ss=ss+'-'+str(a[j+1])
    
    if s==7:
        ss=ss+'=7'
        print(ss)
        exit(0)
