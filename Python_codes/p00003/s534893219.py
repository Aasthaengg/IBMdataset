import sys
n = int(sys.stdin.readline())
for i in range(n):
    sides = [int(k) for k in sys.stdin.readline().split()]
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("YES")
    else:
        print("NO")