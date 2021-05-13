import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()
s_len = len(s)

if s[0] != "A":
    print("WA")
    exit()

cntc = 0

for i in range(2,s_len-1):
    if s[i] == "C":
        cntc += 1

if cntc != 1:
    print("WA")
    exit()

s = s.replace("C", "")
s = s.replace("A", "")

if s_len-2 != len(s):
    print("WA")
    exit()

for i in range(s_len-2):
    if s[i].isupper():
        print("WA")
        exit()

print("AC")