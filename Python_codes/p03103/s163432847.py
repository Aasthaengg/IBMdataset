import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))
ab = sorted([list(map(int,input().split())) for _ in range(n)])
dri_cos = 0

for i in range(n):
    if m >= ab[i][1]:
        dri_cos += ab[i][0]*ab[i][1]
    else:
        dri_cos += ab[i][0]*m
    m -= ab[i][1]
    if m <=0:
        print(dri_cos)
        exit()