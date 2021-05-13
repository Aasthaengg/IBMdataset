x=list(map(int,input().split()))
l=x[0]+x[1]
r=x[2]+x[3]
if l>r:
    print("Left")
elif l==r:
    print("Balanced")
else:
    print("Right")