from sys import stdin

s = stdin.readline().rstrip()
w = int(stdin.readline().rstrip())

print(s[::w])