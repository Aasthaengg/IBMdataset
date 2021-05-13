from collections import defaultdict
from math import gcd
def GCD(a,b):
    gc = gcd(a,b)
    a//=gc
    b//=gc
    return a,b

zero = 0
First_quadrant = defaultdict(int)
Second_quadrant = defaultdict(int)
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        zero +=1
    elif a*b >= 0 and b != 0:
        First_quadrant[(GCD(abs(a),abs(b)))] +=1
    else:
        Second_quadrant[(GCD(abs(b), abs(a)))] +=1
        First_quadrant[(GCD(abs(b), abs(a)))] +=0

ans = 1
for key1, val in  First_quadrant.items():

    v2 = Second_quadrant[key1]
    ans *= (2**val + 2**v2 -1)
    ans %= (10**9+7)
ans  = ans + zero -1
ans %= (10**9+7)
print(ans)
