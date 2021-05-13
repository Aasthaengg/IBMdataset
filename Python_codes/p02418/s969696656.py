from sys import stdin

s = stdin.readline().rstrip()
p = stdin.readline().rstrip()
ss = s*2
if p in ss:
    print("Yes")
else:
    print("No")
