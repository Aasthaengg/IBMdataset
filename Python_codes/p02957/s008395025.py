#Good question
import sys
A,B = map(int,input().split())

if not ( 0 <= A <= 10**9 and 0 <= B <= 10**9 ): sys.exit()

if A % 2 != B % 2:
    print('IMPOSSIBLE')
    sys.exit()
else:
    print(int((A+B)/2))
