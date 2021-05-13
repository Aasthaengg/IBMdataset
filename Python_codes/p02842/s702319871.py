from math import floor
N = int(input())

for x in range(1, 50001):
    if floor(x * 1.08) == N:
        print(x)
        break
else:
    print(":(")