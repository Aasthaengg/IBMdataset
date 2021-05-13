from sys import stdin
N,A,B = [int(x) for x in stdin.readline().rstrip().split()]
if (B - A) % 2 == 0:
    print("Alice")
else:
    print("Borys")