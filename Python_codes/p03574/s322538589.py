h,w=map(int,input().split())
s=[input() for _ in range(h)]
ans=[[] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            cnt=0
            for x,y in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                if 0<=i+x<h and 0<=j+y<w:
                    if s[i+x][j+y]=="#":
                        cnt+=1
            ans[i].append(str(cnt))
        else:
            ans[i].append("#")
for i in range(h):
    print("".join(ans[i]))