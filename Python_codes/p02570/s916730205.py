str = input().split()
if len(str) != 3:
    print("input values is not three")
else:
    a = int(str[0])
    b = int(str[1])
    c = int(str[2])
    if a <= b * c:
         print("Yes")
    else:
         print("No")