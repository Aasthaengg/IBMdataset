import sys
s = input()
t = input()

l = len(s)

if s == t[:l] and len(t) == l+1:
    print("Yes")
else:
    print("No")
