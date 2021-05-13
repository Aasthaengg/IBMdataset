import sys
A,B = map(int,input().split())
if not ( 1 <= A <= 20 and 1 <= B <= 20 ): sys.exit()
print(A + B) if B % A == 0 else print(B - A)