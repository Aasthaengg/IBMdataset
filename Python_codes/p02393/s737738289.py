a = input().split(" ")
temp = a[0]
if a[0] > a[1]:
    temp = a[1]
    a[1] = a[0]
    a[0] = temp
if a[1] > a[2]:
    temp = a[2]
    a[2] = a[1]
    a[1] = temp
if a[0] > a[1]:
    temp = a[1]
    a[1] = a[0]
    a[0] = temp
print(str(a[0]) +" " + str(a[1]) + " " + str(a[2]))
