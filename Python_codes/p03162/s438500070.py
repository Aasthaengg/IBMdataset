import numpy as np

N = int(input())
a = np.zeros((N,3))
for i in range(N):
    a[i][0],a[i][1],a[i][2] = map(int,input().split())

memo = np.zeros((N,3))

memo[0][0], memo[0][1], memo[0][2] = a[0][0],a[0][1],a[0][2]
day = 1

while (day < N):
    memo[day] = [max(memo[day-1][(x+1)%3],memo[day-1][(x+2)%3]) + a[day][x] \
                   for x in [0,1,2]]
    day += 1

print(int(max(memo[day - 1])))