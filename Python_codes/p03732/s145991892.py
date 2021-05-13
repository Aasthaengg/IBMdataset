import sys
input=sys.stdin.readline
n,W=map(int,input().split())
w_1,v=map(int,input().split())
w_list=[[] for i in range(4)]
w_list[0].append(v)
for i in range(n-1):
    w,v=map(int,input().split())
    w_list[w-w_1].append(v)
w_cum=[[] for i in range(4)]
for i in range(4):
    w_list[i].sort(reverse=True)
    Sum=0
    w=w_1+i
    for j in range(len(w_list[i])):
        w_cum[i].append((Sum,w*j))
        Sum+=w_list[i][j]
    w_cum[i].append((Sum,w*len(w_list[i])))
a,b,c,d=len(w_cum[0]),len(w_cum[1]),len(w_cum[2]),len(w_cum[3])
ans=0
for h in range(a):
    for i in range(b):
        for j in range(c):
            for k in range(d):
                weight=w_cum[0][h][1]+w_cum[1][i][1]+w_cum[2][j][1]+w_cum[3][k][1]
                if weight<=W:
                    temp=w_cum[0][h][0]+w_cum[1][i][0]+w_cum[2][j][0]+w_cum[3][k][0]
                    ans=max(ans,temp)
print(ans)
                
        






