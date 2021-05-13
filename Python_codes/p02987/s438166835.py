import sys
s = input()
n = len(s)
for i in range(n):
    if s.count(s[i]) != 2:
        break
else:
    print("Yes")
    sys.exit()
print("No")
