import math;input();a=list(map(int,input().split()));d=a[0]
for i in a:d=math.gcd(i,d)
print(d)