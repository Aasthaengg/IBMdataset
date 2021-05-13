w,a,b=map(int,input().split())
if min(a,b)+w<max(a,b):print(min(abs(a+w-b),abs(b+w-a)))
else:print(0)