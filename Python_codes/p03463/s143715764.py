from sys import stdin

n,a,b = [int(x) for x in stdin.readline().rstrip().split()]

if (b-a)%2 == 1:
    print("Borys")
else:
    print("Alice")