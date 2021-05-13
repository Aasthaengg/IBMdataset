from sys import stdin

a = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()
print(s if a >= 3200 else "red")
