a=[]
for x in input().split(" "):
    a.append(int(x))

if a[1]==1:
    print(0)
else:
    print(a[0]-a[1])