inp = input()
a = inp.split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
a[3] = int(a[3])
a[4] = int(a[4])
if (a[4] <= a[2] and a[2] <= a[0]-a[4]) and (a[4] <= a[3] and a[3] <= a[1]-a[4]):
    print("Yes")
else:
    print("No")
