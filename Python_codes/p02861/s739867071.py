import itertools
import math
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
sum = 0
for i in itertools.permutations(xy, N):
    for j in range(N-1):
       sum += ((i[j][0]-i[j+1][0])**2+(i[j][1]-i[j+1][1])**2)**0.5
print(sum/math.factorial(N))
