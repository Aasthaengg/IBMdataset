import itertools
import math
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

sm=0

for i in itertools.permutations(A):
    for j in range(1,N):
        sm+=(abs(i[j-1][0]-i[j][0])**2+abs(i[j-1][1]-i[j][1])**2)**0.5

print(sm/math.factorial(N))
