import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, a, b, c, d = inintm()
s = input()

if c < d:
    if "##" not in s[a-1:d-1]:
        print("Yes")
    else:
        print("No")
else:
    if ("..." in s[b-2:d+1]) and ("##" not in s[a-1:c-1]):
        print("Yes")
    else:
        print("No")
