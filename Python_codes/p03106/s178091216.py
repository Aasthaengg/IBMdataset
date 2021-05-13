import math

a,b,k=map(int,input().split())

c=math.gcd(a,b)

d=[i for i in range(1,c+1) if c%i==0]

print(d[-k])