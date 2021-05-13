import sys
A,P = map(int,input().split())

if not ( 0 <= A <= 100 and 0 <= P <= 100 ): sys.exit()

print( (A * 3 + P) // 2)