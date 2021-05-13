n = int(input())
a = map(int, input().split())
b1, b2, b4 = 0, 0, 0

for i in a:
    if i % 4 == 0:
        b4 += 1
    elif i % 2 == 0:
        b2 += 1
    else:
        b1 += 1
if b2:
    if b1 <= b4:
        print("Yes")
    else:
        print("No")
else:
    if b1 <= b4 + 1:
        print("Yes")
    else:
        print("No")
