import sys
N,A,B = map(int, input().split())

if B-A == 1:
    print("Borys")
    sys.exit()
elif ((B-A)-1) % 2 == 0:
    print("Borys")
else:
    print("Alice")
