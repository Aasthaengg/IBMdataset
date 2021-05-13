import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()

ans = 0
flag = 0
a = 0

for i in range(len(s)):
    if flag != 1:
        if s[i] == "A":
            flag = 1
            a = i
    elif s[i] == "Z":
        ans = i-a+1

print(ans)