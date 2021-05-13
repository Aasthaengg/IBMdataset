str = raw_input()
q = input()
for i in range(q):
    a = raw_input().split()
    if(a[0] == "print"):
        print(str[int(a[1]):int(a[2]) + 1])
    elif(a[0] == "reverse"):
        str = str[0:int(a[1])] + str[int(a[2]):int(a[1]):-1] + str[int(a[1])] + str[int(a[2]) + 1:]
    elif(a[0] == "replace"):
        str = str[0:int(a[1])] + a[3] + str[int(a[2]) + 1:]