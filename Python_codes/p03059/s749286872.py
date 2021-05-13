import math

a,b,t = map(int,input().split())
t = t+0.5
cnt = t//a

print(math.floor(cnt*b))