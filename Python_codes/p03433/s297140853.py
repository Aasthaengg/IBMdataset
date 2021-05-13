from sys import stdin

n = int(stdin.readline().rstrip())
a = int(stdin.readline().rstrip())

if n%500 - a <= 0:
    print("Yes")
else:
    print("No")
