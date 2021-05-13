def bfs():
    while q!=[]:
        color[q[0]-1]="grey"
        for i in m[q[0]-1]:
            if i==0:continue
            if color[i-1]=="white":
                color[i-1]="grey"
                q.append(i)
                d[i-1]=d[q[0]-1]+1
        del q[0]

n=input()
d=[0]*n
m=[[0]*n for _ in xrange(n)]
info=[0]*n
color=["white"]*n
for i in xrange(n):
    info[i]=map(int,raw_input().split())
    if info[i][1]==0:
        pass
    else:
       for j in info[i][2:]:
           m[info[i][0]-1][j-1]=j
q=[1]
bfs()
for i in xrange(n):
    if i!=0 and d[i]==0:
        print i+1,-1
    else:
        print i+1,d[i]