h,w,d=map(int,input().split())
dic=[0]*(h*w+1)
def cost(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
for i in range(h):
    a=list(map(int,input().split()))
    for j in range(w):
        dic[a[j]]=(i+1,j+1)
dis=[[0] for i in range(d)]
for i in range(d):
    k=1
    for j in range(i+d,h*w,d):
        dis[i].append(dis[i][k-1]+cost(dic[j-d+1],dic[j+1]))
        k+=1
# print(dis)
q=int(input())
ans=0
for i in range(q):
    l,r=map(int,input().split())
    k=l%d-1
    print(dis[k][(r+d-1)//d-1]-dis[k][(l+d-1)//d-1])