from scipy.sparse.csgraph import floyd_warshall

h,w=map(int,input().split(' '))
cost=[list(map(int,input().split(' '))) for _ in range(10)]
dist=floyd_warshall(cost)
cost=[dist[i][1] for i in range(10)]

total=0
for _ in range(h):
    wall=list(map(int,input().split(' ')))
    for num in wall:
        if num==-1 or num==1:
            continue
        total+=cost[num]
print(int(total))