N=int(input())

for h in range(1,3500+1):
    for n in range(1,3500+1):
        try:
            if (N*h*n)%(4*h*n-N*(h+n))==0 and (4*h*n-N*(h+n))>0:
                A,B,C=h,n,(N*h*n)//(4*h*n-N*(h+n))
        except:
            pass
print(A,B,C)