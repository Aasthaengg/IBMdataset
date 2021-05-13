n,Y=input().split(" ")
n=int(n)
Y=int(Y)
y=Y/1000
def counting(n,y):
    u=0
    for a in range(n+1):
        u=n-a
        for b in range(u+1):
            if 9*a+4*b-y+n==0:
                c=n-(a+b)
                a=str(a)
                b=str(b)
                c=str(c)
                l=" ".join([a,b,c])
                return (l)
                break
    else:
        return("-1 -1 -1")
print(counting(n,y))