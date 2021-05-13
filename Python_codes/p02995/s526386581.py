import math
A, B, C, D = map(int, input().split())
lcm = (C * D) // math.gcd(C, D)
waruC = B//C-(A-1)//C
waruD = B//D-(A-1)//D
waruCD = B//lcm-(A-1)//lcm
ans = B-A+1-(waruC+waruD-waruCD)
print(ans)
