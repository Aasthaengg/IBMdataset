n,w=map(int,input().split())
wv=[list(map(int,input().split())) for i in range(n)]
wv.sort(key=lambda x:-x[1])
wv.sort(key=lambda x:x[0])
#print(wv)
w0=wv[0][0]
x=[[0],[0],[0],[0]]
for i in range(n):
    if wv[i][0]==w0:
        k=wv[i][1]+x[0][-1]
        l=len(x[0])
        if l*w0<=w:x[0].append(k)
    elif wv[i][0]==w0+1:
        k=wv[i][1]+x[1][-1]
        l=len(x[1])
        if l*(w0+1)<=w:x[1].append(k)
    elif wv[i][0]==w0+2:
        k=wv[i][1]+x[2][-1]
        l=len(x[2])
        if l*(w0+2)<=w:x[2].append(k)
    else:
        k=wv[i][1]+x[3][-1]
        l=len(x[3])
        if l*(w0+3)<=w:x[3].append(k)
#print(x)
ma=0
for i in range(len(x[3])):
    for j in range(len(x[2])):
        for k in range(len(x[1])):
            for l in range(len(x[0])):
                if i*(w0+3)+j*(w0+2)+k*(w0+1)+l*w0<=w:
                    ma_sub=x[3][i]+x[2][j]+x[1][k]+x[0][l]
                    ma=max(ma,ma_sub)
                else:
                    break
print(ma)
