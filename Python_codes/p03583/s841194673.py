n=int(input())
for a in range(1,3501):
    for b in range(1,3501):
        if (4*a*b-n*b-a*n)!=0:
            c=n*a*b/(4*a*b-n*b-a*n)
            if c>=1 and c.is_integer():
                print(a,b,int(c))
                exit()