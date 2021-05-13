import sys,math,collections,itertools
input = sys.stdin.readline

N,M=list(map(int,input().split()))
road = [0]*(N)
for _ in range(M):
    l,r=map(int,input().split())
    road[l-1]+=1
    road[r-1]-=1
road = list(itertools.accumulate(road))[:-1]

flag=0
for ro in road:
    if ro%2==1:
        print('NO')
        exit()
print('YES')
        

