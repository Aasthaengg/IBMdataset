a=input()
a=[int(x) for x in a.split()]
b=a[0]+a[1]
c=a[2]
print("Yes" if b>c or b==c else "No")