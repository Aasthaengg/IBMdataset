import math

A, B = map(int,input().split())

for i in range(1001):
    if math.floor(i*0.08) == A and math.floor(i*0.10) == B:
        print(i)
        break
else:
    print(-1)