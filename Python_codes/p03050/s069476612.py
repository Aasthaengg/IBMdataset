n=int(input())

t1=2
comb=set()
while t1*t1<=n:
    if n%t1==0:
        t2=n//t1

        m=t1-1
        if t2==n%m:
            comb.add(m)
        m=t2-1
        if t1==n%m:
            comb.add(m)
    t1+=1

if n>2:
    print(sum(comb)+n-1)
else:
    print(sum(comb))