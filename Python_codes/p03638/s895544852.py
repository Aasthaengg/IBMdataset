H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))

color=[]
for i in range(N):
    color+=[i+1]*a[i]

grid=[]
for g in range(H):
    grid.append(color[g*W:(g+1)*W])

for l in range(H):
    if l%2==0:
        print(*grid[l])
    else:
        print(*grid[l][::-1])