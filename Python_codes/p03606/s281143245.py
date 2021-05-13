import sys
N = int(input())
array_list = []
for I in range(N):
    array_list.append(list(map(int,input().split())))

if N < 1 or N > 1000:
    sys.exit()

number = 0
for J in array_list:
    number += (J[1] - J[0] + 1)

print(number)