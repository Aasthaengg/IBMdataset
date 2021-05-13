from itertools import permutations
import math
def dist(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

N = int(input())
X = [list(map(int,input().split())) for _ in range(N)]
A = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = dist(X[i],X[j])
tot = 0
for x in permutations(range(N),N):
    cnt = 0
    for i in range(1,N):
        cnt += A[x[i-1]][x[i]]
    tot += cnt
print(tot/math.factorial(N))