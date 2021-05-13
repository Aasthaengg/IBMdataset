import sys
s = int(input())
if not ( 1 <= s <= 100 ): sys.exit()
array = [s]

for I in range(1,10 ** 6 + 1):
    if array[ I - 1 ] % 2 == 0:
        if array[I - 1]//2 in array:
            print(I + 1)
            sys.exit()
        array.append(array[(I - 1)]//2)     
    else:
        if (3 * array[I - 1]) + 1 in array:
            print(I + 1)
            sys.exit()
        array.append((3 * array[(I - 1)]) + 1)
