h,w,a,b = map(int,input().split())
a= min(w-a,a)
b = min(h-b,b)
for i in range(h):
    if i+1<=b:
        print("0"*a + "1"*(w-a))
    else:
        print("1"*a + "0"*(w-a))
