import math

a,b,c,d=map(int,input().split())
taka=math.ceil(c/b)
aoki=math.ceil(a/d)
print("YNeos"[taka>aoki::2])