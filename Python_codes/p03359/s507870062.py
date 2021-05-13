from sys import stdin

a,b = [int(x) for x in stdin.readline().rstrip().split()]

if a > b:
    print(a-1)
else:
    print(a)