import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()

acgt = ["A", "C", "G", "T"]

ans = ""

for i in range(len(s)):
    t = ""
    for j in range(i, len(s)):
        if s[j] in acgt:
            t += s[j]
        else:
            break
        if len(t) > len(ans):
            ans = t

print(len(ans))
