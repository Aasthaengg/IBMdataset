import sys

input()
for a,b,c in map(lambda x: sorted(map(int,x.split())),sys.stdin.readlines()):
    if a**2 + b**2 == c**2:
        print("YES")
    else:
        print("NO")