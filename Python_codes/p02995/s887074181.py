import math
a,b,c,d = map(int,input().split())

a -= 1
a_b = c * d // math.gcd(c, d)
#print(a_b)
ans_a = a - (a // c + a // d - a // a_b)
ans_b = b - (b // c + b // d - b // a_b)

print(int(ans_b-ans_a))
