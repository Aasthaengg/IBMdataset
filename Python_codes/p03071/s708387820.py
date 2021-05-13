c,d=map(int,input().split())
a=max(c,d)
b=min(c,d)
if a-1>=b:
    print(a+a-1)
else:
    print(a+b)