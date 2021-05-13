import sys

s = input()
t = input()

for i in range(len(s)):
    f = 1
    for j in range(len(s)):
        if s[j] != t[j-i]:
            f = 0
    if f == 1:
        print('Yes')
        sys.exit()

    
print('No')