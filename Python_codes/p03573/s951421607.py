a=input().split()
a=sorted(a)
if a.count(a[0]) == 1:print(a[0])
else:print(a[2])