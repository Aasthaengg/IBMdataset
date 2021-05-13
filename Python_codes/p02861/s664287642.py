import itertools

n = int(input())

p = [[int(i) for i in input().split()] for i in range(n)]

def how_far(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

p_list = list(itertools.permutations(p))

s = 0

for x in p_list:
    for y in range(n-1):
        s += how_far(x[y],x[y+1])

print(s/len(p_list))
