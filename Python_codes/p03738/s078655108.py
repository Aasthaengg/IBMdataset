a=input()
b=input()
if len(a)>len(b):
    print("GREATER")
elif len(a)<len(b):
    print("LESS")
else:
    for i in range(len(a)):
        if int(a[i])>int(b[i]):
            print("GREATER")
            break
        elif int(a[i])<int(b[i]):
            print("LESS")
            break
        else:
            pass
    else:
        print("EQUAL")