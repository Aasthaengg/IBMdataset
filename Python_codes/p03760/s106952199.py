import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

o = input()
e = input()

ans = ""

for i in range(len(e)):
    ans += o[i]
    ans += e[i]

if len(o) - len(e) == 1:
    ans += o[-1]

print(ans)