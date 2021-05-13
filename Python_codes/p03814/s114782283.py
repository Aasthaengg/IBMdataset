# import sys;input = lambda : sys.stdin.readline()
s = input()
A, Z = None, None
for i in range(len(s)):
    if s[i] == "A":
        A = i
        break
for i in range(len(s) - 1, -1, -1):
    if s[i] == "Z":
        Z = i
        break
print(Z - A + 1)
