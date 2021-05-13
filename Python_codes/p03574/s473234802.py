H,W=map(int,input().split())
lst=[]
for i in range(H):
    a=list(input())
    lst.append(a)

for i in range(H):
    for j in range(W):
        if lst[i][j]==".":
            cnt=0
            for h,w in ([0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]):
                nh,nw=i+h,j+w
                if nh<0 or nh>H-1 or nw<0 or nw>W-1:
                    continue
                if lst[nh][nw]=="#":
                    cnt+=1
            lst[i][j]=cnt

for i in range(H):
    print("".join(map(str,lst[i])))