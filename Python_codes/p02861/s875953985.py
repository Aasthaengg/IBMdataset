n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
from itertools import permutations
count = 0
dist = 0
for l in list(permutations(xy)):
    tmp = 0
    for i in range(len(l)-1):
        tmp += ((l[i+1][0]-l[i][0])**2+(l[i+1][1]-l[i][1])**2)**0.5
    dist += tmp
    count += 1

print(dist/count)

