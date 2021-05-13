import sys
N,R = map(int,input().split())

if not ( 1 <= N <= 100 and 0 <= R <= 4111 ): sys.exit()

print(R) if N >= 10 else print(R + 100*(10-N))