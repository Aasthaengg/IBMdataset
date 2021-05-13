h,w,d=map(int,input().split())
grid=[None]*(h*w)
for i in range(h):
    *a,=map(int,input().split())
    for j in range(w):
        grid[a[j]-1]=(i,j)

mp=[[0] for i in range(d)]

for i in range(d):
    tmp=i
    while tmp+d<h*w:
        x=abs(grid[tmp+d][0]-grid[tmp][0])+abs(grid[tmp+d][1]-grid[tmp][1])
        mp[i].append(x+mp[i][-1])
        tmp+=d
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    tmp=mp[r%d][(r-(r%d))//d]-mp[l%d][(l-(l%d))//d]
    print(tmp)