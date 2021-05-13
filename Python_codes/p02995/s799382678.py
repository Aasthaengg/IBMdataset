import math
a,b,c,d=map(int,input().split())
lcm_cd=c*d//math.gcd(c,d)
c_cnt=b//c-(a-1)//c
d_cnt=b//d-(a-1)//d
cd_cnt=b//lcm_cd-(a-1)//lcm_cd
print(b-a+1-c_cnt-d_cnt+cd_cnt)