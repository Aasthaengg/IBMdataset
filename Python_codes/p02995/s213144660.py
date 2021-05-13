import math
A, B, C, D = map(int, input().split())
calc = lambda x: B//x-(A-1)//x
print((B-A+1)-calc(C)-calc(D)+calc(C*D//math.gcd(C, D)))