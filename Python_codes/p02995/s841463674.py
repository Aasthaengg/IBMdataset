from fractions import gcd
def lcm(x,y):return x*y//gcd(x,y)

a,b,c,d = map(int,input().split())
total =b-a+1##総数
cnum= b//c-(a-1)//c##cの倍数
dnum =b//d-(a-1)//d##dの倍数
m = lcm(c,d)
mnum = b//m -(a-1)//m##最小公倍数の倍数

print(total-(cnum+dnum-mnum))