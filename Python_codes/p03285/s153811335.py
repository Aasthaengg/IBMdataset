import sys

N = int(input())
for cake in range(30):
    for donut in range(15):
        if 4*cake+7*donut == N:
            print('Yes')
            sys.exit()

print('No')