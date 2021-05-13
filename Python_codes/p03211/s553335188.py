import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()

base = 753
ans = 1000

for i in range(len(s)-2):
    if abs(base - int(s[i:i+3])) < ans:
        ans = abs(base - int(s[i:i+3]))

print(ans)
