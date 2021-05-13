n=int(input())
for a in range(1,3*n//4+1):
    if n>=4*a:
        continue
    b = a
    while True:
        if n*(a+b)>=4*a*b:
            b+=1
            continue
        x = a*b*n
        y = 4*a*b-n*(a+b)
        if y>0 and x%y==0:
            c = x//y
            print("{} {} {}".format(a,b,c))
            exit(0)
        if x/y<b:
            break
        b+=1