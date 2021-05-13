h,w,a,b = (int(i) for i in input().split())
for i in range(b): print("1"*a+"0"*(w-a))
for i in range(h-b): print("0"*a+"1"*(w-a))