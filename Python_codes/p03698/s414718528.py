import sys
s = input()
s = sorted(s)

for i in range(1,len(s)):
    if s[i] == s[i-1]:
        print('no')
        sys.exit()
print('yes')