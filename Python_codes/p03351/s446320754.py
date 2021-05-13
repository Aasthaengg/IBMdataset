a=list(map(int,input().split()))
b=a[:3]
c=sorted(b)
if abs(b[2]-b[0])<=a[3] or (abs(b[2]-b[1])<=a[3] and abs(b[1]-b[0])<=a[3]):print("Yes")
else:print("No")