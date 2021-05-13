a=input()
b=a.split()
d=list()
for c in b:
    d.append(int(c))
W=d[0]
H=d[1]
x=d[2]
y=d[3]
r=d[4]
if W-r>=x>=0 and H-r>=y>=0:
    print("Yes")
else:
    print("No")
