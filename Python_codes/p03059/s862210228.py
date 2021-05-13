import math
a,b,t=map(int, input().split())
T=t+0.5
ans=math.ceil(T//a)
print(ans*b)