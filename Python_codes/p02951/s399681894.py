import math
a,b,c = (int(x) for x in input().split())
if c > a-b:
    print (c-(a-b))
else :
    print (0)