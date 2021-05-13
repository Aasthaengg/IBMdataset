def dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])
N = int(input())
X = [list(map(int,input().split())) for _ in range(N)]
flag = 0
t1 = 0
x1,y1 = 0,0
for i in range(N):
    t2,x2,y2 = X[i]
    dt = t2-t1
    d = dist((x1,y1),(x2,y2))
    if dt>=d and (dt-d)%2==0:
        t1,x1,y1 = t2,x2,y2
        continue
    flag = 1
    break
if flag==0:
    print("Yes")
else:
    print("No")