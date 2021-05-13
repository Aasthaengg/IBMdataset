import sys
n = int(input())

for i in range(n, 0, -1):
    if (i**0.5).is_integer():
        print(i)
        sys.exit()