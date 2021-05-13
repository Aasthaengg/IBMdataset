n,x,y = map(int, open(0).read().split())

x,y = sorted([x,y])

def calc(a,b):
    a,b = sorted([a,b])
    return min(b-a, abs(b-y)+1+abs(x-a))

ans = [0]*(n-1)

from itertools import combinations

for a,b in combinations(range(1,n+1),2):
    ans[calc(a,b)-1] += 1

for c in ans:
    print(c)