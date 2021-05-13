import math
L, R = map(int, input().split())
m = 2018
for i in range(L, min(L+2018, R)+1):
    for j in range(i+1, min(i+2019, R)+1):
        m = min(m, i*j%2019)
print(m)
