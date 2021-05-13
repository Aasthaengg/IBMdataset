import math

a, b, c, d = map(int, input().split())

lcm = c*d // math.gcd(c, d)

dif = b-a+1
div_c = b//c - (a-1)//c
div_d = b//d - (a-1)//d
div_cd = b//lcm - (a-1)//lcm

ans = dif - (div_c + div_d) + div_cd
print(int(ans))