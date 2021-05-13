#problems1
N=int(input())
d=[]
for _ in range(N):
    x,y=map(int,input().split())
    d.append((x,y,x+y))
d.sort(key=lambda x:-x[2])
t=0
a=0
for i in range(N):
    if i%2==0:
        #高橋くん
        t+=d[i][0]
    else:
        a+=d[i][1]
print(t-a)    