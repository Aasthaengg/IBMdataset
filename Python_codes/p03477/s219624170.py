from sys import stdin
A,B,C,D = [int(x) for x in stdin.readline().rstrip().split()]
if A+B > C+D:
    print("Left")
elif A+B < C+D:
    print("Right")
else:
    print("Balanced")