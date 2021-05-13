H,W,N=map(int,input().split())
s=set()
for i in range(N):
    a,b=map(lambda x:int(x)-1,input().split())
    s.add((a,b))
count=[0]*10

for x,y in s:
    for tx in range(x-2,x+1):
        for ty in range(y-2,y+1):
            if tx<0 or ty<0 or tx+2>=H or ty+2>=W:
                continue
            cnt=0
            for nx in range(tx,tx+3):
                for ny in range(ty,ty+3):
                    if (nx,ny) in s:
                        cnt+=1
            count[cnt]+=1
count=[0]+[count[i]//i for i in range(1,10)]
count[0]=(H-2)*(W-2)-sum(count)
print(*count,sep='\n')