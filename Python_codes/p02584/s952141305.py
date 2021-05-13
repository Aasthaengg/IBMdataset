x,k,d=map(int,input().split())
b,c=abs(x%d),abs(-x%d)
mi=min(b,c)
if b<=c:
    a=abs(x//d)
else:
    a=abs(-x//d)
if k<a:
    print(min(abs(x-k*d),abs(x+k*d)))
else:
    if a%2==k%2:
        print(mi)
    else:
        print(min(abs(mi-d),abs(mi+d)))
