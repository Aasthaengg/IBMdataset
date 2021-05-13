from collections import defaultdict
N = int(input())
d = defaultdict(int)
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            n = x*x+y*y+z*z+x*y+y*z+z*x
            d[n]+=1
for i in range(1,N+1):
    print(d[i])