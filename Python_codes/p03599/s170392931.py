from fractions import gcd

A,B,C,D,E,F=map(int,input().split())

sugar=[]
g=gcd(C,D)
for i in range(0,3000):
    if i>=C*D and i%g==0:
        sugar.append(i)

for i in range(0,D):
    for j in range(0,C):
        if C*D>i*C+j*D:
            sugar.append(i*C+j*D)

sugar.sort()

ans=(-1,1)
for i in range(F//(100*A)+1):
    for j in range(F//(100*B)+1):
        if F>100*A*i+100*B*j:
            x=F-(100*A*i+100*B*j)
            y=(A*i+B*j)*E
            sugarupper=min(x,y)

            start=0
            end=len(sugar)
            while end-start>1:
                test=(end+start)//2
                if sugarupper>=sugar[test]:
                    start=test
                else:
                    end=test

            if sugarupper>=sugar[end]:
                s=sugar[end]
            else:
                s=sugar[start]

            m,n=ans
            if n*s>m*(100*A*i+100*B*j+s):
                ans=(s,100*A*i+100*B*j+s)

print(ans[1],ans[0])
