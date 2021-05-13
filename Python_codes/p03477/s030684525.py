from sys import stdin

a,b,c,d = [int(x) for x in stdin.readline().rstrip().split()]

k = a+b
j = c+d

if k < j:
    print("Right")
elif k == j:
    print("Balanced")
else:
    print("Left")