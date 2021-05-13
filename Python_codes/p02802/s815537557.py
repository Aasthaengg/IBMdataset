n,m=map(int,input().split())
k=[0]*(n+1)
wa_count=0
ac_count=0
for i in range(m):
    p,s=map(str,input().split())
    if s== "AC":
        if k[int(p)]!=-1:
            wa_count=wa_count+k[int(p)]
            k[int(p)]=-1
            ac_count += 1
    else:
        if k[int(p)]!=-1:
            k[int(p)]+= 1
            
ac=str(ac_count)
wa=str(wa_count)
print(ac+" "+wa)