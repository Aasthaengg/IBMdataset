a=input()
a=[int(x) for x in a.split()]
print(a[0] if a[1]==a[2] else a[1] if a[0]==a[2] else a[2])
