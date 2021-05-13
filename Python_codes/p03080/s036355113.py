from sys import stdin

n = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()

if s.count("R") > s.count("B"):
    print("Yes")
else:
    print("No")