import sys
c = [i for i in input().split()]
ab = int(c[0]+c[1])
for i in range(int(100100**0.5)+1):
    if i**2 == ab:
        print("Yes")
        sys.exit(0)

print("No")