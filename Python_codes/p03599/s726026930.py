a,b,c,d,e,f = map(int, input().split())
mx=0
swmx=100*a
smx=0
 
for i in range(0,31):
    for j in range(0,31):
        for k in range(0,51):
            for l in range(0,51):
                w=0
                s=0
                w+=100*a*i+100*b*j
                s+=c*k+d*l
                if w+s<=f and s<=e*w/100 and w!=0 and mx<100*s/(w+s):
                    mx=100*s/(w+s)
                    swmx=w+s
                    smx=s
print(swmx,smx)