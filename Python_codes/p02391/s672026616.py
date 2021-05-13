a = input().split(" ")
b = a[1]

if int(a[0]) > int(a[1]):
    print("a > b")
elif int(a[0]) < int(a[1]):
    print("a < b")
else:
    print("a == b")