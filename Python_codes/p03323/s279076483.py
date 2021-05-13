from sys import stdin
A, B = [int(x) for x in stdin.readline().rstrip().split()]
if A<=8 and B<=8:
    print("Yay!")
else:
    print(":(")