from math import gcd
a, b, c, d = map(int, input().split())
whole = b - a + 1
sum_c = b//c - (a-1)//c
sum_d = b//d - (a-1)//d
div = (c*d)//gcd(c, d)
sum_c_d = b//div - (a-1)//div
print(whole - ((sum_c + sum_d) - sum_c_d))