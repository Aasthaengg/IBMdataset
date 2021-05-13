h,w,d = map(int, input().split())
a=[list(map(int,input().split())) for i in range(h)]

q=int(input())
lr=[list(map(int,input().split())) for i in range(q)]

from collections import defaultdict
zahyo = defaultdict(list)
for i in range(h):
    for j in range(w):
        zahyo[a[i][j]-1] = [i,j]

rui=[0]*(h*w + 10)
for i in range(d,h*w):
    last=zahyo[i-d]
    now = zahyo[i]

    dist = abs(last[0]-now[0]) + abs(last[1]-now[1])
    rui[i] = rui[i-d] + dist

for que in lr:
    l,r=que
    print(rui[r-1]-rui[l-1])