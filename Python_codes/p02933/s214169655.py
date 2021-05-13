from sys import stdin

a = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()

if a >= 3200:
    print(s)
else:
    print('red')