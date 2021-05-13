import math
h,w,d = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]
lis = [[0,0] for i in range(h * w)]
num = [[0] * math.ceil((h * w) // d + 1) for i in range(d)]
for i in range(h):
    for j in range(w):
        lis[a[i][j]-1] = [i,j]
for i in range(h * w-d):
    num[i%d][i//d+1] = num[i%d][i//d]+abs(lis[i][0]-lis[i+d][0])+abs(lis[i][1]-lis[i+d][1])
q = int(input())
for _ in range(q):
    now,goal = map(int,input().split())
    if now % d == 0:
        print(num[now%d-1][(goal-now%d)//d-1]-num[now%d-1][(now-now%d)//d-1])
    else:
        print(num[now%d-1][(goal-now%d)//d]-num[now%d-1][(now-now%d)//d])
