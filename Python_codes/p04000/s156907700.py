import sys

input=sys.stdin.readline

H,W,N=map(int,input().split())
point=set([])
ans=[0 for i in range(0,10)]
ans[0]=(H-2)*(W-2)

def black(x,y):
    ans=0
    if (x-1,y-1) in point:
        ans+=1
    if (x-1,y) in point:
        ans+=1
    if (x-1,y+1) in point:
        ans+=1

    if (x,y-1) in point:
        ans+=1
    if (x,y) in point:
        ans+=1
    if (x,y+1) in point:
        ans+=1

    if (x+1,y-1) in point:
        ans+=1
    if (x+1,y) in point:
        ans+=1
    if (x+1,y+1) in point:
        ans+=1
        
    return ans

for _ in range(0,N):
    a,b=map(int,input().split())
    if a>2:
        if b>2:
            ss=black(a-1,b-1)
            ans[ss]-=1
            ans[ss+1]+=1

        if W>b>1:
            ss=black(a-1,b)
            ans[ss]-=1
            ans[ss+1]+=1

        if W-1>b:
            ss=black(a-1,b+1)
            ans[ss]-=1
            ans[ss+1]+=1
    if H>a>1:
        if b>2:
            ss=black(a,b-1)
            ans[ss]-=1
            ans[ss+1]+=1

        if W>b>1:
            ss=black(a,b)
            ans[ss]-=1
            ans[ss+1]+=1

        if W-1>b:
            ss=black(a,b+1)
            ans[ss]-=1
            ans[ss+1]+=1

    if H-1>a:
        if b>2:
            ss=black(a+1,b-1)
            ans[ss]-=1
            ans[ss+1]+=1
        if W>b>1:
            ss=black(a+1,b)
            ans[ss]-=1
            ans[ss+1]+=1

        if W-1>b:
            ss=black(a+1,b+1)
            ans[ss]-=1
            ans[ss+1]+=1

    point.add((a,b))

for i in range(0,10):
    print(ans[i])
