a,b,c,d,e,f = map(int,input().split())
a,b,e = 100*a,100*b,e/(100+e)
best = [max(0,(f//a)*a,(f//b)*b),0,0] #[sugarwater,sugar,concentration]

for n in range(f//a+1):
    na = n*a
    for m in range((f-na)//b+1):
        if n==m==0:
            continue
        mb = m*b
        for k in range((f-na-mb)//c+1):
            kc = k*c
            for l in range((f-na-mb-kc)//d+1):
                ld = l*d
                sugar = (kc+ld)
                sugarwater = (na+mb+kc+ld)
                if best[2] < sugar/sugarwater <= e:
                    best = [sugarwater,sugar,sugar/sugarwater]
                
best.pop()
print(*best)