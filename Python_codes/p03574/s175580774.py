h,w=map(int,input().split())
l=[["."]*(w+2)]
for i in range(h):
    l.append(list("."+input()+"."))
l.append(["."]*(w+2))

tate=[-1,-1,-1,0,0,1,1,1]
yoko=[-1,0,1,-1,1,-1,0,1]

for i in range(1,h+1):
    l2=[]
    for j in range(1,w+1):
        if l[i][j]=="#":
            l2.append("#")
        else:
            cnt=0
            for k in range(8):
                if l[i+tate[k]][j+yoko[k]]=="#":
                    cnt+=1
            l2.append(str(cnt))
    print("".join(l2))