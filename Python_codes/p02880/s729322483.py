import sys
N = int(input())
array = [ I for I in range(1,10) ]

if not ( 1 <= N <= 100 ): sys.exit()

for J in range(1,10):
    for K in range(1,10):
        if N == J*K:
            print('Yes')
            sys.exit()
print('No')