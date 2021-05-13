import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
stp = []
chp = []
for i in range(n):
    stp.append(list(map(int,input().split())))
for i in range(m):
    chp.append(list(map(int,input().split())))
for i in range(n):
    mdis =[]
    for j in range(m):
        mdis.append(abs(stp[i][0]-chp[j][0])+abs(stp[i][1]-chp[j][1]))
    print(mdis.index(min(mdis))+1)
