import math
a,b,c,d=map(int,input().split())
cd = c*d // math.gcd(c,d)
# b以下のc,d,cdの倍数の個数からa未満のc,d,cdの倍数個数をそれぞれ引く
s_c = b//c - (a-1)//c
s_d = b//d - (a-1)//d
s_cd = b//cd - (a-1)//cd
print((b-a+1)-s_c-s_d+s_cd)