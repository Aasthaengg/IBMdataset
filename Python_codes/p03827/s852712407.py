import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
s = input()

x = 0
ans = 0

for i in range(n):
    if s[i] == "I":
        x += 1
        if x > ans:
            ans = x
    else:
        x -= 1

print(ans)
