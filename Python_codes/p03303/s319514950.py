from sys import stdin
s = stdin.readline().rstrip()
n = int(stdin.readline().rstrip())
print(s[::n])