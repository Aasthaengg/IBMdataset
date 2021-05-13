import sys
N = int(input())

if not ( 1 <= N <= 100 ): sys.exit()

print(N//2) if N % 2 == 0 else print(N//2 + 1)