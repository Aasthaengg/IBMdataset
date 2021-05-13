h,w=map(int,input().split())
li=[input() for _ in range(h)]
for i in range(h):
    res=""
    for j in range(w):
        cnt=0
        if li[i][j]==".":
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0<=i+x<h and 0<=j+y<w and li[i+x][j+y]=="#":
                        cnt+=1
            res+=str(cnt)
        else:
            res+="#"
    print(res)