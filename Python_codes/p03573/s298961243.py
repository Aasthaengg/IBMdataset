a=sorted([int(i) for i in input().split()])
b,c=a[0],a[2]
print(b if a.count(b)==1 else c)