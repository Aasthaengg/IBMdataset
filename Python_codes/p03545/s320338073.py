s = input()
op1 = "+"
op2 = "-"

a = [0 for _ in range(8)]
a[0] = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3])
a[1] = int(s[0]) + int(s[1]) + int(s[2]) - int(s[3])
a[2] = int(s[0]) + int(s[1]) - int(s[2]) + int(s[3])
a[3] = int(s[0]) + int(s[1]) - int(s[2]) - int(s[3])
a[4] = int(s[0]) - int(s[1]) + int(s[2]) + int(s[3])
a[5] = int(s[0]) - int(s[1]) + int(s[2]) - int(s[3])
a[6] = int(s[0]) - int(s[1]) - int(s[2]) + int(s[3])
a[7] = int(s[0]) - int(s[1]) - int(s[2]) - int(s[3])

if a[0] == 7:
    print(s[0]+op1+s[1]+op1+s[2]+op1+s[3]+"=7")
    exit()
elif a[1] == 7:
    print(s[0]+op1+s[1]+op1+s[2]+op2+s[3]+"=7")
    exit()
elif a[2] == 7:
    print(s[0]+op1+s[1]+op2+s[2]+op1+s[3]+"=7")
    exit()
elif a[3] == 7:
    print(s[0]+op1+s[1]+op2+s[2]+op2+s[3]+"=7")
    exit()
elif a[4] == 7:
    print(s[0]+op2+s[1]+op1+s[2]+op1+s[3]+"=7")
    exit()
elif a[5] == 7:
    print(s[0]+op2+s[1]+op1+s[2]+op2+s[3]+"=7")
    exit()
elif a[6] == 7:
    print(s[0]+op2+s[1]+op2+s[2]+op1+s[3]+"=7")
    exit()
elif a[7] == 7:
    print(s[0]+op2+s[1]+op2+s[2]+op2+s[3]+"=7")
    exit()
