import math
c,a,b=map(int,input().split())
s=(a+b+c)/2
print(int(math.sqrt(s*(s-a)*(s-b)*(s-c))))