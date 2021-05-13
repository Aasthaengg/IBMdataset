import sys,math,collections,itertools
input = sys.stdin.readline

N=int(input())
xy = []

if N == 1:
    print(1)
    exit()

for _ in range(N):
    xy.append(list(map(int,input().split())))

rxy = []
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        rxy.append((xy[i][0]-xy[j][0],xy[i][1]-xy[j][1]))
cr = collections.Counter(rxy)
print(N-max(cr.values()))

