import sys
n = int(input())

if n%4 == 0 or n%7 == 0:
    print('Yes')
else:
    for i in range(n//4+1, 0, -1):
        j = 0
        while i*4+j*7 < n:
            j += 1
        if i*4+j*7 == n:
            print('Yes')
            sys.exit()
    print('No')
