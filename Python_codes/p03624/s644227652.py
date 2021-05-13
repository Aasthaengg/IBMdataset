import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()
sl = []

for i in range(len(s)):
    sl.append(s[i])

for i in range(97, 123):
    if chr(i) not in sl:
        print(chr(i))
        exit()

print("None")
