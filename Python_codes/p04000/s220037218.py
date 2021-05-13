from collections import defaultdict
Delta = [-1,0,1]
d = defaultdict(lambda:0)
def paint(d,x,y):
    for dx in Delta:
        for dy in Delta:
            d[(x+dx,y+dy)] += 1
H,W,N = map(int,input().split())
for i in range(N):
    a,b = map(int,input().split())
    paint(d,a,b)
ans = defaultdict(lambda:0)
for x,y in d.keys():
    if 2<=x<=H-1 and 2<=y<=W-1:
        ans[d[(x,y)]] += 1
ans0 = (H-2)*(W-2)
for i in range(10):
    ans0 -= ans[i]
ans[0] = ans0
for i in range(10):
    print(ans[i])