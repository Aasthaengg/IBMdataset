a,b,c,d,e,f=map(int,input().split())

ans,index=0,[a*100,0]
base=100*e/(100+e)
for i in range(31):
    for j in range(31):
        for k in range(101):
            for l in range(101):
                w=i*100*a+j*100*b
                s=c*k+d*l
                if w==0:continue
                if w+s>f:break
                den=s*100/(w+s)
                if den<=base and ans<den:
                    ans=den
                    index=[w+s,s]

print(*index)