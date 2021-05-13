from collections import defaultdict
H,W,N = map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(N)]

d = defaultdict(lambda:0)
def count(a,b):
    for dx1 in [-1,0,1]:
        for dy1 in [-1,0,1]:
            x,y = a+dx1,b+dy1
            if 2<=x<H and 2<=y<W:
                d[(x,y)] += 1

for i in range(N):
    count(*ab[i])

ans = defaultdict(lambda:0)
for x,y in d:
    ans[d[(x,y)]] += 1

ans[0] = (H-2)*(W-2)
for i in range(1,10):
    ans[0] -= ans[i]

for i in range(10):
    print(ans[i])