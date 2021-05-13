import sys
D = int(input())

if not (22 <= D <= 25):
    sys.exit()

print("Christmas",end='')
for I in range(25-D):
    print(" Eve",end='')