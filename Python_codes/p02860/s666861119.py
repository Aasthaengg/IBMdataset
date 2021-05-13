import sys
N = int(input())
S = input()

if not ( 1 <= N <= 100 ): sys.exit()
if not S.islower(): sys.exit()
if not ( len(S) == N ): sys.exit()
if N % 2 == 1: print('No'); sys.exit()
print('Yes') if ( S[:N//2] + S[:N//2] == S ) else print('No')