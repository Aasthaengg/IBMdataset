n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i] == t[0]:
        if s[i:] == t[:n-i]: break
if s[i] != t[0]: i += 1
print(len(s[:i]+t))