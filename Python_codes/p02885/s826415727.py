import sys
A,B = map(int,input().split())

if not ( 1 <= A <= 100 and 1 <= B <= 100 ): sys.exit()
if not ( isinstance(A,int) and isinstance(B,int) ): sys.exit()

print( A - (B * 2)) if A - (B * 2) >= 0 else print(0)

