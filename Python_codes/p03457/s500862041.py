import sys
input = sys.stdin.readline

N=int(input())

txy = [[0,0,0]]
for _ in range(N):
    txy.append(list(map(int,input().split())))
txy.sort()

dtxy = []
for i in range(N):
    dt=txy[i+1][0]-txy[i][0]
    dx=txy[i+1][1]-txy[i][1]
    dy=txy[i+1][2]-txy[i][2]
    ds = dt-abs(dx)-abs(dy)
    if ds<0 or ds%2 !=0:
        print('No')
        exit()
print('Yes')
