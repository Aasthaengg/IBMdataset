import itertools
import math
n = int(input())
m = math.factorial(n)
l = [list(map(int,input().split())) for i in range(n)]
x,y = [list(i) for i in zip(*l)]
z = list(range(n))
z = list(itertools.permutations(z))
ans = 0
for i in range(m):
    for j in range(n - 1):
        ans += math.sqrt((x[z[i][j]] - x[z[i][j+1]]) ** 2 + (y[z[i][j]] - y[z[i][j+1]]) ** 2)
print(ans / m)