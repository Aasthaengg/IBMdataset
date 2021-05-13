import sys
input=sys.stdin.readline

n,k=map(int,input().split())
xy=[tuple(map(int,input().split())) for _ in range(n)]
X=sorted(set(xy[i][0] for i in range(n)))
Y=sorted(set(xy[i][1] for i in range(n)))


from itertools import combinations

ans=10**20
for x1,x2 in combinations(X,2):
    for y1,y2 in combinations(Y,2):
        c=0
        for x,y in xy:
            if x1<=x<=x2 and y1<=y<=y2:
                c+=1
        if c>=k:
            ans=min(ans,(x2-x1)*(y2-y1))
print(ans)
