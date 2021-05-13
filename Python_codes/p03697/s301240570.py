from sys import stdin
a,b = [int(x) for x in stdin.readline().rstrip().split()]

if a + b >= 10:
    print("error")
else:
    print(a+b)