from math import floor as fl

A,B =map(int,input().split())

for i in range(10000):
    if fl(i * 8 / 100) == A and fl(i / 10) == B:
        print(i)
        break
else:
    print(-1)