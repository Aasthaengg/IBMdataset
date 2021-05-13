a = input().split()
x = 0
if a[0] == "1" and a[1] == "1":
    x = 1000000
elif a[0] == "1":
    x = x + 300000
elif a[1] == "1":
    x = x + 300000
if a[0] == "2":
    x = x + 200000
if a[0] == "3":
    x = x + 100000
if a[1] == "2":
    x = x + 200000
if a[1] == "3":
    x = x + 100000
print(x)