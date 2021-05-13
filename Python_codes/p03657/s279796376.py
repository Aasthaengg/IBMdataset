from sys import stdin
A,B = [int(x) for x in stdin.readline().rstrip().split()]
f = False
if A % 3 == 0:
    f = True
if B % 3 == 0:
    f = True
if (A+B) % 3 == 0:
    f = True
if f:
    print("Possible")
else:
    print("Impossible")