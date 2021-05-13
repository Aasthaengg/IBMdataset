ABC = input().split()
a = int(ABC[0])
b = int(ABC[1])
c = int(ABC[2])
if a<b:
    if b<c:
        print("Yes")
    else:
        print("No")
else:
    print("No")