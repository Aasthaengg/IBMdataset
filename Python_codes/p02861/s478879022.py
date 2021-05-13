import itertools
import math
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
distance=[]
f=list(itertools.permutations(list(range(1,n+1))))
for i in range(len(f)):
    length=0
    for j in range(1,n):
        length+=math.sqrt((l[f[i][j]-1][0]-l[f[i][j-1]-1][0])**2+(l[f[i][j]-1][1]-l[f[i][j-1]-1][1])**2)
    distance.append(length)
print(sum(distance)/len(distance))