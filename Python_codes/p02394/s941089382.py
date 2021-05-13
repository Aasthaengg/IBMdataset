n=raw_input()
k=n.split(" ")

W=int(k[0])
H=int(k[1])
x=int(k[2])
y=int(k[3])
r=int(k[4])
f=0

if 0<=x-r<=x+r<=W:
  if 0<=y-r<=y+r<=H:
    print "Yes"
    f=1
if f==0:
  print "No"