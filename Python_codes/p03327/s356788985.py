import sys
N = int(input())

if not ( 1 <= N <= 1998 ):
    sys.exit()

print('ABD') if N > 999 else print('ABC')