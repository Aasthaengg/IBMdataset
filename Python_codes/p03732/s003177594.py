n,w=list(map(int,input().split()))
gds=[list(map(int,input().split())) for _ in range(n)]

dp={0:0}

for cw,cv in gds:
    tmp={}

    for key,value in dp.items():
        if key in tmp:
            tmp[key]=max(tmp[key],value)
        else:
            tmp[key]=value
        
        if cw+key<=w:
            if cw+key in tmp:
                tmp[cw+key]=max(tmp[cw+key],value+cv)
            else:
                tmp[cw+key]=value+cv
    
    dp=tmp

print(max(dp.values()))
