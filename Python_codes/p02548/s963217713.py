import math
N = int(input())

cnt =0
for a in range(1,N):
    cnt += math.floor((N-1)/a)

print(cnt)