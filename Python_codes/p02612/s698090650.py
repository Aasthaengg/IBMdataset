import sys
N=int(input())

for i in range(1, 12):
    if 1000*i-N>=0:
        print(1000*i-N)
        sys.exit()
