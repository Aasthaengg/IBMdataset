import sys
s = input()
ans = 'AC'
c = 0
if s[0] != 'A':
    ans = "WA"
for i in range(2,len(s)-1):
    if "C" == s[i]:
        c += 1
if c != 1:
    ans = "WA"
c = 0
for i in range(len(s)):
    a = ord(s[i])
    if 65 <= a and a <= 96:
        c += 1
if c != 2:
    ans = "WA"
print(ans)