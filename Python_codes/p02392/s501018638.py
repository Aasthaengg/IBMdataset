l1 = list(input().split(" "))
a = int(l1[0])
b = int(l1[1])
c = int(l1[2])
if a<b:
    if b<c:
        print("Yes")
    else:
        print("No")
else:
    print("No")