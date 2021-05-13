import sys
T,X = map(int,input().split())
if not ( 1 <= T <= 100 and 1 <= X <= 100 ): sys.exit()

print(T/X)