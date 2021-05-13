s=input().split()
W=int(s[0])
H=int(s[1])
x=int(s[2])
y=int(s[3])
r=int(s[4])
if r<=x<=W-r and r<=y<=H-r:
    print("Yes")
else:
    print("No")
