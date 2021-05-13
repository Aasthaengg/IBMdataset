import sys
A,B,C = map(int,input().split())
if not ( 1 <= B <= 20 and B <= A <= 20 ): sys.exit()
if not ( 1 <= C <= 20 ): sys.exit()

res =  C - (A - B)
print(res) if res >= 0 else print(0) 