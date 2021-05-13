from itertools import permutations
from math import sqrt, factorial
n = int(input())
lst = [None]

for _ in range(n):
    x,y = map(int,input().split())
    lst.append([x,y])

ans = 0

for per in permutations(list(range(1,n+1))):
    lenth = 0
    for i in range(0,n-1):
        x1,y1 = lst[per[i]]
        x2,y2 = lst[per[i+1]]
        lenth += sqrt((x2-x1)**2 + (y2-y1)**2)
    ans += lenth

ans /= factorial(n)

print(ans)
