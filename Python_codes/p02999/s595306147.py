from sys import stdin

x,a = [int(x) for x in stdin.readline().rstrip().split()]

if x < a:
    print(0)
else:
    print(10)