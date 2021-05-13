a,b,c,d,e,f = map(int, input().split())
mx=0
swmx=a*100
smx=0
 
for i in range(0,31):
    for j in range(0,31):
        for k in range(0,1000):
            for l in range(0,1000):
                w=0
                s=0
                w+=100*a*i+100*b*j
                s+=c*k+d*l
                targ=w+s
                if targ>f:
                    break
                elif targ==0:
                    break
                elif s>e*w/100:
                    break
                elif  mx<s/(w+s):
                    mx=s/targ
                    swmx=targ
                    smx=s
print(swmx,smx)