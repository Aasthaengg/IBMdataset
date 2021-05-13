n,m = map(int, input().split())
import itertools
array = []

for i in range(n):
    s = list(map(int, input().split()))
    array.append(s)

res = 0
ans = 0
for a,b,c in itertools.product([1,-1],repeat=3):
    tmp = []
    for x,y,z in array:
        tmp.append(a*x+b*y+z*c)
    tmp.sort(reverse=True)
    ans = max(ans,sum(tmp[:m]))

print(ans)
