import sys
N = int(input())

for i in range(1,10):
    if N <= int(str(i)*3):
        print(str(i)*3)
        sys.exit()