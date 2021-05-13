import math
A, B, C, D = map(int, input().split())

c = (B//C) - ((A+C-1)//C) + 1
d = (B//D) - ((A+D-1)//D) + 1
lcm = int(C * D / math.gcd(C, D))
m = (B//lcm) - ((A+lcm-1)//lcm) + 1
ans = (B-A+1) - (c+d-m)
print(int(ans))