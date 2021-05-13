h, w=map(int,input().split())
c=[list(map(int,input().split())) for i in range(10)]

def warshall_floyd(c):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                c[j][k]=min(c[j][k], c[j][i]+c[i][k])

    mn_c=[c[s][1] for s in range(10)]
    return mn_c

mn_c=warshall_floyd(c)

sm=0
for i in range(h):
    a=list(map(int,input().split()))
    for k in a:
        if k>=0:
            sm+=mn_c[k]

print(sm)