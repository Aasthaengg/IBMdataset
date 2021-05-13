import sys
x,y = map(int,input().split())

if x <= 0 or x >= 13 or y <= 0 or y >= 13:
    sys.exit()
if x >= y:
    sys.exit()

A = (1, 3, 5, 7, 8, 10, 12)
B = (4, 6, 9, 11)

if x == 2 or y == 2:
    print("No")
    sys.exit()
if x in A and y in A:
    print("Yes")
elif x in B and y in B:
    print("Yes")
else:
    print("No")