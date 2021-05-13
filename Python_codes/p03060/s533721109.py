n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
xy = [x-y for (x,y) in zip(v,c)]
sm = 0
for x in xy:
    sm = sm+x if x>0 else sm+0
print(sm)