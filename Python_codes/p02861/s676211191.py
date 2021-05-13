import math
import itertools

N = int(input())
L = []
cnt = 0

for i in range(N):
    xy = list(map(int, input().split()))
    L.append(xy)

for i in itertools.permutations(L,N):
    for j in range(len(i)-1):
        cnt += math.sqrt((i[j][0] - i[j+1][0])**2 + (i[j][1] - i[j+1][1])**2)

print(cnt / math.factorial(N))