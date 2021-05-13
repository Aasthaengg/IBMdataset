import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()
t = input()

for _ in range(len(s)):
    s = s[-1] + s[:len(s)-1]
    if s == t:
        print("Yes")
        exit()

print("No")