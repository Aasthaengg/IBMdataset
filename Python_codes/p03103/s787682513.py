import math
N,M = map(int, input().split())
l = [[int(i) for i in input().split()] for j in range(N)]

l.sort()
count = 0
i = 0
while(M > 0):
    M -= l[i][1]
    count += l[i][0]*l[i][1]
    if(M < 0):
        count -= abs(M)*l[i][0]
    i += 1
print(count)