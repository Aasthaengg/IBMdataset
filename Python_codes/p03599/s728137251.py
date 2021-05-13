A,B,C,D,E,F=list(map(int,input().split()))
max=0
satou=0
water=0
for i in range(31):
    for j in range(31):
        for k in range(101):
            for l in range(101):
                a=100*A*i+100*B*j
                s=C*k +D*l
                if a==0:break
                if a+s<=F and (a/100)*E>=s :
                    if max<100*s/(a+s):
                        max=100*s/(a+s)
                        water=a+s
                        satou=s
if satou>0:
    print(water,satou)
else:
    print(100*A,0)