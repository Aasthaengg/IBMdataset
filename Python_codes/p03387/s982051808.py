li = list(map(int,input().split()))
su = sum(li)
ma = max(li)

if su%2 == ma%2:print(int((ma*2-(su-ma))/2))
else:print(int(((ma+1)*2-(su-ma)+1)/2))