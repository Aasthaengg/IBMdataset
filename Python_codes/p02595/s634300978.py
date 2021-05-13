import math
N, D = map(int, input().split())
i = 0
count = 0
while (i < N):
    p, q = map(int, input().split())
    d = math.sqrt(p*p + q*q)
    if (d <= D):
        count+= 1
    i+= 1
print(count)