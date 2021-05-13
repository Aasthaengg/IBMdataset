import math
a,b,c,d = map(int,input().split())
min_c = (a-1)//c
max_c = b//c
min_d = (a-1)//d
max_d = b//d
tmp = (c * d) // math.gcd(c, d)
min_cd = (a-1)//tmp
max_cd = b//tmp

#print(a,b,c,d)
#print(min_c,max_c)
#print(min_d,max_d)
#print(min_cd,max_cd)
print(b-(a-1)-(max_c-min_c)-(max_d-min_d)+(max_cd-min_cd))