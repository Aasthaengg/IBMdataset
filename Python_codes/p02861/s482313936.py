import itertools
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

way = 0
p_list = [i for i in range(n)]
for P in itertools.permutations(p_list):
    for i in range(n-1):
        way += ((xy[P[i+1]][1]-xy[P[i]][1])**2+(xy[P[i+1]][0]-xy[P[i]][0])**2)**0.5

kai = 1
for i in range(n):
    kai *= (i+1)

print(way/kai)