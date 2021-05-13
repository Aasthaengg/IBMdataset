import sys
array = [0,0,0,0,0,0]
for I in range(len(array)):
    array[I] = int(input())
    if not ( 0 <= array[I] <= 123 ):
        sys.exit()
print('Yay!') if (array[4] - array[0]) <= array[-1] else print(':(')