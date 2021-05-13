from sys import stdin

s = stdin.readline().rstrip()
n = int(stdin.readline().rstrip())

s = s[::n]

print(s)