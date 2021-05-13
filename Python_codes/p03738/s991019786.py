from sys import stdin

a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())

if a > b:
    print("GREATER")
elif a == b:
    print("EQUAL")
else:
    print("LESS")