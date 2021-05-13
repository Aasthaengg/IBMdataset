S = int(input())
import math

if S == 10**18:
    print(0,0,10**9,0,0,10**9)
else:
    Y3 = S // 10**9 + 1
    X3 = 10**9 - S % 10**9

    print(0,0,10**9,1,X3,Y3)