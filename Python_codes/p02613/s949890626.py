import numpy

N = int(input().strip())

grid = []
for i in range(N):
    grid.append(input().strip())

count_array = [0,0,0,0]
for i in grid:
    if i == "AC":
        count_array[0] += 1
    elif i == "WA":
        count_array[1] += 1
    elif i == "TLE":
        count_array[2] += 1
    else:
        count_array[3] += 1

print("AC x", count_array[0])
print("WA x", count_array[1])
print("TLE x", count_array[2])
print("RE x", count_array[3])