import math
from itertools import permutations
n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in permutations(list(range(n))):
    for j in range(n-1):
        ans += math.sqrt((xy[i[j]][0]-xy[i[j+1]][0])**2+(xy[i[j]][1]-xy[i[j+1]][1])**2)
print(ans/(math.factorial(n)))