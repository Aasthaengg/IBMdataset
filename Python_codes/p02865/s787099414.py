n = int(input())
import sys
if n == 1 or n == 2:
    print(0)
    sys.exit()
if n % 2 == 0:
    print(n//2 - 1)
else:
    print(n//2)