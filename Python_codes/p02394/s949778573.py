ia = [int(i) for i in input().split(" ")]
W=ia[0]
H=ia[1]
x=ia[2]
y=ia[3]
r=ia[4]
print("Yes" if 0<=x-r and x+r<=W and 0<=y-r and y+r<=H else "No")