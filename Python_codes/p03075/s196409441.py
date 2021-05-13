import math
l=[]
f=0
for i in range(5):
    z=int(input())
    l.append(z)
k=int(input())
for i in range(4):
    for j in range(1,5):
        if math.fabs(l[i]-l[j])>k:
            f=1
            break
if f==1:
    print(":(")
else:
    print("Yay!")
