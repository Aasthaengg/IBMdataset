a = input()

b = a[0]+a[0]+a[0]
c = a[1]+a[1]+a[1]

if (b in a) or (c in a):
    print("Yes")
else:
    print("No")