import sys
nums, alice, borys = map(int,input().split())
if nums == 2:
    print("Borys")
    sys.exit()

if alice > borys:
    space = alice - borys-1
else:
    space = borys - alice-1

if space % 2 == 0:
    print("Borys")
elif space % 2 == 1:
    print("Alice")