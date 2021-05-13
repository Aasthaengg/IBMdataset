s = input()
a = "abcdefghijklmnopqrstuvwxyz"

for i in s:
    a = a.replace(i, "")
else:
    if len(a):
        print(a[0])
    else:
        print("None")