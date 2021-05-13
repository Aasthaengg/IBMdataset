n,x,*l=map(int,open(0).read().split())
c,d=1,0
for i in range(n):
    d+=l[i]
    if d>x:
        print(c)
        break
    else:
        c+=1
else:
    print(c)