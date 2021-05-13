a = input()
a = a.split()
b = int(a[1])
c = int(a[2])
d = int(a[3])
a = int(a[0])
e = a / d
f = c / b
if int(e) < e:
    e = int(e + 1)
if int(f) < f:
    f = int(f + 1)
if e >= f:
    print("Yes")
else:
    print("No")