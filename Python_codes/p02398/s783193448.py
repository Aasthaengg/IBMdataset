import math

a,b,c = [int(i) for i in input().split()]

cnt = 0
for i in range(a, b+1):
    if math.floor(c/i) == math.ceil(c/i):
        cnt = cnt + 1

print(cnt)

