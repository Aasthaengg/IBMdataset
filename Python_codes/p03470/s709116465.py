import sys
N = int(input())
array = []
for I in range(N):
    array.append(int(input()))

if not ( 1 <= N <= 100 ):
    sys.exit()
for J in range(len(array)):
    if not ( 1 <= array[J] <= 100 ):
        sys.exit()

print(len(set(array)))