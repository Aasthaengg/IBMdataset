d = list(map(int,(input().strip().split(' '))))
a = d[0]
b = d[1]
c = d[2]
if a == b:
    if a == c:
        print("Yes")
    else:
        print("No")
else:
    print("No")