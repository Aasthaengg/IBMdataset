from sys import stdin
data = stdin.readlines()

old = data[0].split()[0]
new = data[1].split()[0]

if len(new) == len(old) + 1 and new.startswith(old):
    print("Yes")
else:
    print("No")