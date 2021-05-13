a=input()
b=a.split()
d=list()
for c in b:
    d.append(int(c))

a=d[0]
b=d[1]
c=d[2]
if a<b<c:
    print("Yes")
else:
    print("No")
