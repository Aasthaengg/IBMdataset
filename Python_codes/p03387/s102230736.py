a,b,c=map(int,input().split())
p = max(a,b,c)
q = min(a,b,c)
r = a+b+c-(p+q)
x =(p-q)//2+(p-r)//2
q +=((p-q)//2)*2
r +=((p-r)//2)*2
if p == q and p == r:
        print(x)
elif p != q and p != r:
        print(x+1)
else:
        print(x+2)