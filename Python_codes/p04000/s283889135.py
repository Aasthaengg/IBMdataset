h,w,n=map(int,input().split())
black=[tuple(map(int,input().split())) for _ in range(n)]
sblack=set(black)
ans=[0]*10
for a,b in black:
    for x in range(3):
        for y in range(3):
            cnt=0
            ok=True
            for nx,ny in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
                dx,dy=nx-x,ny-y
                if 1<=a-dx<=h and 1<=b-dy<=w:
                    if (a-dx,b-dy) in sblack:
                        cnt+=1
                else:
                    ok=False
                    break
            if ok:
                ans[cnt]+=1
for i in range(1,10):
    ans[i]//=i
ans[0]=(h-2)*(w-2)-sum(ans[1:])
for num in ans:
    print(num)