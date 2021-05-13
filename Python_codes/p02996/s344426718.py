import sys
import math


N = int(input())

timelis = []
for _ in range(N):
    A,B = map(int, input().split())
    timelis.append([A,B])

timelis = sorted(timelis,key=lambda x: x[1])

sum_time = 0
for i in timelis:
    need = i[0]
    deadline = i[1]

    sum_time = sum_time + need

    if sum_time > deadline:
        print("No")
        sys.exit()

print("Yes")
