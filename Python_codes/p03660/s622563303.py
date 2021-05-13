import sys
sys.setrecursionlimit(2000000)
def input():
    return sys.stdin.readline()[:-1]
n=int(input())
ab=[list(map(int,input().split())) for i in range(n-1)]
ki=[[] for i in range(n+1)]
for i in range(n-1):
    ki[ab[i][0]].append(ab[i][1])
    ki[ab[i][1]].append(ab[i][0])
# print(ki)
kyori=[[float("INF"), float("INF")] for i in range(n+1)]
def tansaku(m, dis, hito):
    q=[[m,dis]]
    while q:
        po=q.pop()
        for i in ki[po[0]]:
            if kyori[i][hito]>po[1]:
                kyori[i][hito]=po[1]
                q.append([i,po[1]+1])

tansaku(1,1,0)
tansaku(n,1,1)
fe,su=0,0

for i in range(1,n+1):
    if kyori[i][0]<=kyori[i][1]:
        fe+=1
    else:
        su+=1

if fe>su:
    print("Fennec")
else:
    print("Snuke")