import sys
n = int(input())

count = 0
for i in range(int(100/4)+1):
    for j in range(int(100/7)+1):
        if n == 4*i+7*j:
            print('Yes')
            sys.exit(0)

print('No')
