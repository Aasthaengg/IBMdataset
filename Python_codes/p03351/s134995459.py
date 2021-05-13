x=list(map(int,input().split()))
if abs(x[0]-x[2])<=x[3] or (abs(x[0]-x[1])<=x[3] and abs(x[2]-x[1])<=x[3]):
    print("Yes")
else:
    print("No")