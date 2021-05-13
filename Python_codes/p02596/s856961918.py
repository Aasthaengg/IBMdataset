import math

k = int(input())
value = 7

isTrue = 0
for i in range(1, 10**6):
    if value % k == 0:
        isTrue = 1
        print(i)
        break
    value = (value * 10 + 7) % k

if not isTrue:
    print(-1)