import itertools
import math

n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
dist = 0

route = list(itertools.permutations([i for i in range(n)]))
for num in route:
    for i in range(1,n):
        dist += math.sqrt((xy[num[i]][0]-xy[num[i-1]][0])**2+ (xy[num[i]][1]-xy[num[i-1]][1])**2)
    
print(dist/len(route))