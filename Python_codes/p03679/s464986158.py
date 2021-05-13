x,a,b = map(int,input().split())
print("delicious"*(a>=b) or "safe"*((x+a)>=b) or "dangerous")