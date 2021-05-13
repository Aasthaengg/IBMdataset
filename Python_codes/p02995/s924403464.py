import math
A,B,C,D = map(int,input().split())
count1 = 0
count2 = 0
ans1 = B-B//C-B//D+B//((C*D)//math.gcd(C,D))
A = A-1
ans2 = A-A//C-A//D+A//((C*D)//math.gcd(C,D))
print(ans1-ans2)