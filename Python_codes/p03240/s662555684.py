def resolve():
    n=int(input())
    xyh=[[0]*3 for _ in range(n)]
    for i in range(n):
        x,y,h=map(int,input().split())
        xyh[i][0],xyh[i][1],xyh[i][2]=h,x,y
    xyh.sort(reverse=True)
    ans,flg=0,0
    for cx in range(101):
        for cy in range(101):        
            ans,flg=0,0
            for h,x,y in xyh:
                if ans==0:
                    if h==0:
                        continue
                    else:
                        ans=h+abs(x-cx)+abs(y-cy)
                else:
                    if h==0:
                        if ans>abs(x-cx)+abs(y-cy):
                            flg=1
                            break
                        else:
                            continue
                    else:
                        if ans==h+abs(x-cx)+abs(y-cy):
                            continue
                        else:
                            flg=1
                            break
            if flg==0:
                break
        if flg==0:
            break
    print(cx,cy,ans)            

if __name__ == '__main__':
    resolve()