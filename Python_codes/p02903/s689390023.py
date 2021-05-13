h,w,a,b=map(int,input().split())
s = "0"*a+"1"*(w-a)
t = "1"*a+"0"*(w-a)
for _ in range(h-b):
    print(s)
for _ in range(b):
    print(t)