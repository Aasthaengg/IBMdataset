a = input()
b = input()
if len(a) > len(b):
    print("GREATER")
elif len(b) > len(a):
    print("LESS")
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        if int(a[i]) > int(b[i]):
            print("GREATER")
            exit()
        else:
            print("LESS")
            exit()
    else:
        print("EQUAL")
