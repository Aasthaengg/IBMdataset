from sys import stdin

a,b = [int(x) for x in stdin.readline().rstrip().split()]

if a % 3 == 0 or b % 3 == 0 or (a+b)%3 == 0:
    print("Possible")
else:
    print("Impossible")