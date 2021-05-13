N=int(input())

if N%4==0:
    print(3*N//4,3*N//4,3*N//4)
else:
    f=False
    a=(N+3)//4
    while a<=3*N//4:
        if f:
            break
        b=a
        while b<=2*N*a//(4*a-N):
            num=N*a*b
            den=4*a*b-N*(a+b)
            if den<=0:
                b+=1
                continue
            if num%den==0:
                c=num//den
                print(a,b,c)
                f=True
                break
            b+=1
        a+=1