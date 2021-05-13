a = int(input())
b = int(input())

flag1 = True
flag2 = True
flag3 = True

if a == 1:
    flag1 = False
elif a == 2:
    flag2 = False
elif a == 3:
    flag3 = False
    
if b == 1:
    flag1 = False
elif b == 2:
    flag2 = False
elif b == 3:
    flag3 = False
    
if flag1:
    print(1)
elif flag2:
    print(2)
else:
    print(3)
