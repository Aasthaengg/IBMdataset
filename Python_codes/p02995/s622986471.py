import math
A,B,C,D = map(int, input().split())
ans1 = B-B//C-B//D
g = math.gcd(C, D)
l = C*D//g
ans1 = ans1+B//l
ans2 = A-1-(A-1)//C-(A-1)//D
ans2 = ans2+(A-1)//l
ans = ans1-ans2
print(int(ans))
