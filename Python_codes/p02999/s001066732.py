import sys
X,A = map(int,input().split())

if not ( 0 <= X <= 9 and 0 <= A <= 9 ): sys.exit()

print(0) if X < A else print(10)