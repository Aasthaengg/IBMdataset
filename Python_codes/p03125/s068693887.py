from sys import stdin

a,b = [int(x) for x in stdin.readline().rstrip().split()]

if b%a == 0:
    print(a+b)
else:
    print(b-a)