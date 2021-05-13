h,w,d=map(int,input().split())
a=[ list(map(int,input().split())) for _ in range(h) ]
q=int(input())
cost=[0 for _ in range(h*w+1)]
pos=dict()
l=[]
for i in range(h):
    for j in range(w):
        pos[a[i][j]]=[i,j]
        l.append((a[i][j],i,j))
l.sort()
for val,x,y in l:
    if val-d<=0:
        cost[val]=0
    else:
        cost[val]=cost[val-d]+abs(pos[val][0]-pos[val-d][0])+abs(pos[val][1]-pos[val-d][1])
#print(l)
for _ in range(q):
    l,r=map(int,input().split())
    print(cost[r]-cost[l])
