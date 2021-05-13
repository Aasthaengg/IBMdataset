def inp():return map(int,input().split())

a,b=inp()
if b%a==0:print(a+b)
else:print(b-a)