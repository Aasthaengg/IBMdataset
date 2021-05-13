z = input()
w,x,y = z.split()
a,b,c = int(w),int(x),int(y)

if a < b and b < c:
    print("Yes")
else:
    print("No")