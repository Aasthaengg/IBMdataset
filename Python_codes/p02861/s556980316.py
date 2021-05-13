import itertools
import math

n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]

l = range(n)

d_list =[]

for v in itertools.permutations(l):
    d = 0
    for i in range(n-1):
        f = v[i]
        t = v[i+1]
        d += math.sqrt((xy[t][0] - xy[f][0]) ** 2 + (xy[t][1] - xy[f][1]) ** 2)
    d_list.append(d)

print(sum(d_list) / math.factorial(n))