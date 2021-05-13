n=int(input())
a=[0 for i in range(100001)]
for i in range(1,41):
    a[6*(i**2)]+=1
for i in range(1,99):
    for j in range(1,i):
        if 3*(i**2)+j**2+2*i*j<=10000:
            a[3*(i**2)+j**2+2*i*j]+=3
        if 3*(j**2)+i**2+2*i*j <=10000:
            a[3*(j**2)+i**2+2*i*j]+=3
for i in range(1,100):
    for j in range(1,i):
        if i**2+j**2+i*j+i+j>9999:
            break
        for k in range(1,j):
            if i**2+j**2+k**2+i*j+i*k+j*k>10000:
                break
            else:
                a[i**2+j**2+k**2+i*j+i*k+j*k]+=6
for i in range(1,n+1):
    print(a[i])