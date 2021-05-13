a = list(input())
b = list(input())
c = 0
if len(a) > len(b):
    c = 1
elif len(a) < len(b):
    c = 2
else:
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            c = 1
            break
        elif int(a[i]) < int(b[i]):
            c = 2
            break
if c == 0:
    print("EQUAL")
elif c == 1:
    print("GREATER")
else:
    print("LESS")