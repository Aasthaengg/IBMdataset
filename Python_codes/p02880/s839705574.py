import sys
N = int(input())
array = [ I for I in range(1,10) ]

if not ( 1 <= N <= 100 ): sys.exit()

if N >= 82:
    print('No'); sys.exit()
else:
    for J in array:
        if (N % J) == 0 and (N // J) <= 9 : print('Yes'); sys.exit()
print('No')