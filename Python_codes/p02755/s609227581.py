import math
A, B = map(int, input().split())
for i in range(1,1010):
    a, b = i*0.08, i*0.1
    if math.floor(a) == A and math.floor(b) == B:
        print(i)
        break

    if i == 1009:
        print(-1)