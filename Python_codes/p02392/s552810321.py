inp = input()
a = inp.split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
if a[0] < a[1] and a[1] < a[2]:
    print("Yes")
else:
    print("No")
