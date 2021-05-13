import sys
A,B,C = map(int,input().split())
if not ( 1 <= A <= 100 and 1 <= B <= 100 and 1 <= C <= 100 ): sys.exit()

print( C ) if A * C <= B else print( B // A )