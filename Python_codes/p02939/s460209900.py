import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()

ans = 0
a = ""
b = ""

for i in range(len(s)):
    a += s[i]
    if a == b:
        continue
    ans += 1
    b = a
    a = ""

print(ans)