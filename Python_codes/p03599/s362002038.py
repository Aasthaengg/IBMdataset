A,B,C,D,E,F=map(int,input().split())
A,B=A*100,B*100
water=[]
for i in range(F//A+1):
    for j in range(F//B+1):
        if A*i+B*j<=F and not(i==0 and j==0):
            water.append((A*i+B*j))
water=list(set(water))
ans=[water[0],0]
mconc=0
sugar=[]
for x in water:
    sugar.append(min(F-x,(x*E//100)))
for w,s in zip(water,sugar):
    for i in range(s//C+1):
        j=(s-C*i)//D
        cap=(C*i+D*j)
        if(cap/(w+cap))*100>mconc:
            mconc=(cap/(w+cap))*100
            ans=[w+cap,cap]
print(*ans)