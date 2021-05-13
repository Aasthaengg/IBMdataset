import sys

x = [0 for i in range(26)]
c0 = 97
for line in sys.stdin:
    for c in line.strip('\n').lower():
        if 'a' <= c and c <= 'z':
            x[ord(c)-c0] += 1

for i in range(26):
    print '%s : %d' %(chr(i + c0), x[i])