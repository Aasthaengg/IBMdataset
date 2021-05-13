import sys
A,B,C = map(int,input().split())
if not ( 1 <= A <= 100 and 1 <= B <= 100 and 1 <= C <= 100 ): sys.exit()
if not ( isinstance(A,int) and isinstance(B,int) and isinstance(C,int) ): sys.exit()

print(( A * B ) // 2)