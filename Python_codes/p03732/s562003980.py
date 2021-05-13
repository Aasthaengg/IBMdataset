n,W=map(int,input().split())
wv=[list(map(int,input().split())) for i in range(n)]
data=[[] for i in range(4)]
w1=wv[0][0]
for u in wv:
    w,v=u
    data[w-w1].append(v)
for i in range(4):
    data[i].sort(reverse=True)
    data[i]=[0]+data[i]
    for j in range(1,len(data[i])):
        data[i][j]+=data[i][j-1]
a=len(data[0])
b=len(data[1])
c=len(data[2])
d=len(data[3])
ans=0
for i in range(a):
    for j in range(b):
        for k in range(c):
            for l in range(d):
                if w1*i+(w1+1)*j+(w1+2)*k+(w1+3)*l<=W:
                    ans=max(ans,data[0][i]+data[1][j]+data[2][k]+data[3][l])
print(ans)