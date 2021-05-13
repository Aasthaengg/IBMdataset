a,b,c,d = map(int,input().split())

divc = b//c-(a-1)//c
divd = b//d-(a-1)//d
import math
l = c*d//math.gcd(c,d)
divl = b//l-(a-1)//l
print(b-a+1-divc-divd+divl)
